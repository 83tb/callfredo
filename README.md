callfredo
=========

Quick start
-----------

<pre>
cd callfredo
virtualenv --distribute --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
cp localsettings.py{.template,}
./manage.py runserver
</pre>

Go to http://localhost:8000/ Should work!