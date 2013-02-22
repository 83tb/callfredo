callfredo
=========

Callfredo = Facebook + Twilio. It will call users and ask them to record happy birthday wishes, and then post it to their Facbeook Wall.



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
