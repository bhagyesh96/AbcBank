# Features
>> Contain One Portals for Two type of users
   > Bank User
   > Customer

>> Customer
   > Can View Balance ond user Detail
   > Can do fund transfer to other user
   > can add voucher fund
   > can get statment in Excel file in custom timeframe
   > will get email notification on every transection

>> Bank User
   > can get statement of any  customer time frame in exel format by using account number

# Technology Used
   >> Front End:
      >Bootstrap,HTML,css
   >> Backed :
      >python 3 and django 3


# Setup Instruction

>> navigate to main project folder where manage.py is present
>> in settings.py change email server coniguration
>> Run Commands
   >>>"pip3 install -r requitement.txt"
   >>>"python3 manage.py makemigrations" to create migrations
   >>>"python3 manage.py migrate" to apply migrations
   >>>"python3 manage.py createsuperuser" to create superuser(optional)
>> you run application on any server
   >>>  run command "python3 manage.py runserver" for default django server

## Guide to project for Customer
>> navigate to "localhost:8000" or port you have selected
>> show option to register and sign
>> register yourselt it will redirect you to register and then redirect you to login page
>> login with your credentials
>> you will see all functionalities specified  

## Guide to project for Bank User
>> navigate to "localhost:8000" or port you have selected
>> show option to register and sign
>> register yourselt it will redirect you to register and then redirect you to login page
>> login with your credentials
>> then go to admin panel "localhost:8000/admin"
>> change your profile role to Bank user
>> now if you login with same calender you will login as manager and get new options in left side   bar 