# GoogleAlerts
This will store google alerts in pdf in cloud. it requires Pango and Cairo if its running on pythonanwhere.com. The below outlines the process:

wget http://cairographics.org/releases/cairo-1.8.10.tar.gz
tar xzf cairo-1.8.10.tar.gz
cd cairo-1.8.10
./configure --prefix=$HOME/.local
make
make install

- After the above installation set LD environment in bashrc:

