from . import app, login_manager
from .models.database import session
from .models.group import Group
from .models.students import Student
from .models.user import User
from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user


@app.route("/main")
@app.route("/group_management")
def group_management():
    all_groups = session.query(Group).all()
    all_groups = [x.name_of_group for x in all_groups]
    return render_template("group.html", groups=all_groups)


@app.route("/main")
@app.route("/group_management", methods=["POST"])
@login_required
def group_management():
    name_of_group = request.form.get("name_of_group")
    group = Group(
        name_of_group=name_of_group
    )
    try:
        session.add(group)
        session.commit()
    except Exception as exc:
        return f"При збереженні групи виникла проблема: {exc}"
    finally:
        session.close()
        return redirect("group_management")


@app.route("/student_management/<group_name>")
def group_list(group_name):
    group_id = session.query(Group).where(Group.name_of_group == group_name).first().id
    group = session.query(Student).where(Student.group_id == group_id).all()
    return render_template("student.html", group=group)


@app.route("/student_management/<group_name>", methods=["POST"])
@login_required
def group_list(group_name):
    group_id = session.query(Group).where(Group.name_of_group == group_name).first().id
    name = request.form["name"]
    surname = request.form["surname"]
    age = request.form["age"]
    home_address = request.form["home_address"]

    student = Student(
        name=name,
        surname=surname,
        age=int(age),
        home_address=home_address,
        gr_id=group_id
    )
    try:
        session.add(student)
        session.commit()
    except Exception as exc:
        return f"При збереженні виникла проблема - {exc}"
    finally:
        session.close()
        return redirect(f"/student_management/{group_name}")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]

        user = session.query(User).where(User.username == username).first()

        if user:
            flash("Цей користувач вже існує!")
            return redirect("login")

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        try:
            session.add(new_user)
            session.commit()
        except Exception as exc:
            return f"При збереженні користувача виникла помилка: {exc}"
        finally:
            session.close()
            return redirect("/login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]
        remember = True if request.form["remember"] else False

        user = session.query(User).where(User.username == username).first()
        if not user or not check_password_hash(user.password, password):
            flash("Будь ласка, перевірте свій логін та пароль і спробуйте знову!")
            return redirect("/login")
        login_user(user=user, remember=remember)
        return redirect(url_for("main"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("main")


@login_manager.user_loader
def load_users(user_id):
    return session.query(User).get(int(user_id))