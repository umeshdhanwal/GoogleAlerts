# GoogleAlerts
This will store google alerts in pdf in cloud. it requires Pango and Cairo if its running on pythonanwhere.com. The below outlines the process:

wget http://cairographics.org/releases/cairo-1.8.10.tar.gz
tar xzf cairo-1.8.10.tar.gz
cd cairo-1.8.10
./configure --prefix=$HOME/.local
make
make install

- After the above installation set LD environment in bashrc:
source ~/.bashrc
vim ~/.bashrc

Add the below line at the end: 
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.local/lib

The Google alerts for specific websites can be created by using Feed43:

for e.g. for website thephoenix.ie the below pattern can be used which will extract all the links: 

- Global Search Pattern:
{%}

- Item Repeatbale search Pattern:
<h6 class="issuem-featured-thumb-title headline">{*}
<a href="{%}"{*}
</h6>


