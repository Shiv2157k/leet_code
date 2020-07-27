import functools


user = {"username": "jose", "access_level": "admin"}


# make secure is called as decorator.
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function


def get_admin_password__():
    return "1234"


@make_secure
def get_admin_password_():
    return "1234"


@make_secure
def get_password_(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


# decorators with parameters
# make secure is called as decorator.
def make_secure_(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."
        return secure_function
    return decorator


@make_secure_("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure_("user")
def get_dashboard_password():
    return "user: user_password"


get_admin_password = make_secure(get_admin_password)
user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())
print(get_admin_password_())
print(get_password_("billing"))
print(get_admin_password_.__name__)



