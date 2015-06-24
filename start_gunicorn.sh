APPNAME=mysite
APPDIR=/home/ubuntu/$APPNAME/

LOGFILE=$APPDIR'gunicorn.log'
ERRORFILE=$APPDIR'gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=ec2-52-74-90-224.ap-southeast-1.compute.amazonaws.com:8000
USER=ubuntu

cd /home/ubuntu/mysite/


exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE 1>>$ERRORFILE &
