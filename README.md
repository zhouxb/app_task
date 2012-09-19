==============================================
app_task: task for project template
==============================================

Provides task to a project template.

INSTALL
============
1. Install Project Template

  django-admin.py startproject --template=https://github.com/zhouxb/project_template/zipball/master [project_name]

2. Install App Account

  pip install https://github.com/zhouxb/app_task/zipball/master

3. Add account to INSTALLED_APPS in settings.py

  INSTALLED_APPS = {

    ...

    tasking,

  }

4. Add tasking url in urls.py

  url(r'tasking/', include('tasking.urls')),

5. Create DB

  python manage.py schemamigration tasking --init

  python manage.py migrate loggit

