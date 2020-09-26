from django.core.mail import send_mail
from  django.conf import settings



def SendTransactionEmail(email,amount,acno):
    try:
        send_mail(
        'Transaction to : '+str(acno) +" for amount :"+str(amount)+" Rs is Successful",
        'Transaction Details: \nReciever : '+str(acno)+"\namount : "+str(amount) +"\nemail : "+str(email),
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
        return {"type":"success",
                "message":"email sending success"
            } 
    except:
        return {
            "type":"error",
            "message":"email sendin failed"
            }    
