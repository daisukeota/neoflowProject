# neoflowProject
neoflow.org
* deploy
+ docker-compose run django /code/manage.py collectstatic
+ docker-compose up
+ /etc/cont-init.d/11-set-nginx-env
+ /etc/init.d/nginx reload

or
+ sudo chown root:root 11-set-nginx-env
