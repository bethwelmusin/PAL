from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Companies(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    agent =models.ForeignKey('Agents', null=True, on_delete=models.PROTECT)


class Agents(models.Model):
    First_name = models.CharField(max_length=200, null=True)
    Last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    #Deals= models.ManyToOneRel(Deals)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)


class Leads(models.Model):
    APPROVED = 'a'
    PENDING = 'p'
    REJECTED = 'r'



    STATUS = (
        (APPROVED, 'approved'),
        (PENDING, 'pending'),
        (REJECTED, 'rejected'),
    )

    lead_name = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Companies, null=True, on_delete=models.SET_NULL)
    company_representative = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    products = models.CharField(max_length=200, null=True)
    product_cost = models.FloatField(null=True)
    agent = models.ForeignKey('Agents', null=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default=PENDING)
    notes = models.CharField(max_length=200, null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)




class Deals(models.Model):

    STATUS = (
        ('won', 'won'),
        ('lost', 'lost'),
        ('closed', 'closed'),
    )


    name = models.CharField(max_length=200, null=True)
    product = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    #contact = models.CharField(max_length=200, null=True)
    #email = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Companies, null=True, on_delete=models.SET_NULL)
    agent_responsible = models.ForeignKey(Agents, null=True, on_delete=models.SET_NULL)
    deal_status = models.CharField(max_length=200, null=True, choices=STATUS)
    quote = models.CharField(max_length=200, null=True , blank=True)
    lead = models.OneToOneField(Leads, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)



class Contacts(models.Model):
    First_name = models.CharField(max_length=200, null=True)
    Last_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Companies, null=True, on_delete=models.SET_NULL)
    agent = models.ForeignKey(Agents, null=True, on_delete=models.SET_NULL)
    profile_picture = models.ImageField()

