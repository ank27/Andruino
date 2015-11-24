import datetime as dt
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question_text=models.CharField(max_length=200)
    published_date=models.DateField('date published')
    QUESTION_TYPE=(('N','New'),('O','Old'))
    question_type=models.CharField(max_length=5,choices=QUESTION_TYPE, default='N')
    score=models.DecimalField(null =True, max_digits=5,decimal_places=2)

    #From MyApplication.models import *
    # q=Question.objects.all() calls def __str__
    # q.get(id=1) gives first Question object
    def __str__(self):
        return '%s  %s %s %s' %(self.question_text, self.published_date, self.question_type, self.score)
        # return self.question_text


    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)

    def is_question_type(self):
        return self.question_type
        # was_published_recently.admin_order_field= 'published_date'
        # was_published_recently.boolean=True
        # was_published_recently.short_discription='Published recently?'

    def score_value(self):
        return self.score


class Choice(models.Model):
    question=models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


    def vote_count(self):
        return self.votes

##CharField is used when we need to define max_length of field
##TextField is used when there is no limit,
## for larger field we use textField
##IntegerField() has default value =0
##Avoid using null values in Char and TextField

# class Musician(models.Model):
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     instrument=models.CharField(max_length=50)
#     track=models.TextField(max_length=100)
#
# class Album(models.Model):
#     artist=models.ForeignKey(Musician)
#     name=models.CharField(max_length=20)
#     release_date=models.DateField()
#     num_stars=models.IntegerField()
#     is_available=models.BooleanField(default=False)

class UserInfo(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField()
    user_contact=models.CharField(max_length=10)
    user_password=models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s' %(self.user_name, self.user_email, self.user_password)

    def user_detail(self):
        return '%s %s %s %s' %(self.user_name, self.user_email, self.user_contact,self.user_password)

    def user_contact_detail(self):
       return self.user_contact

    def user_password_detail(self):
        return self.user_password

    def user_email_detail(self):
       return self.user_email


class TopicInfo(models.Model):
    topic_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)
    topic_image=models.ImageField(upload_to='static/images/', blank=True, null=True)
    def __str__(self):
        return '%s' %(self.topic_name)

    def isActive(self):
        return '%s' %(bool(self.is_active))

    def image_preview(self):
        if self.topic_image:
            return u'<img src="%s" width="100dp" height="100dp"/>' % self.topic_image.url
        else:
            return 'No image'
    image_preview.short_description='Thumb'
    image_preview.allow_tags = True


class SubTopic(models.Model):
    topic=models.ForeignKey(TopicInfo,verbose_name="Topic Name")
    subTopic_name=models.CharField(max_length=50,verbose_name='Sub Topic Name')
    subTopic_isactive=models.BooleanField(default=False, verbose_name='Active')
    isTheory_active=models.BooleanField(default=False, verbose_name='Theory')
    isFormula_active=models.BooleanField(default=False, verbose_name='Formula')
    isQuestion_active=models.BooleanField(default=False, verbose_name='Question')

    def __str__(self):
        return '%s %s' %(self.topic,self.subTopic_name)

    def subtopic_active(self):
        return '%s' %(bool(self.subTopic_isactive))
    def theory_active(self):
        return '%s' %(bool(self.isTheory_active))
    def formula_active(self):
        return '%s' %(bool(self.isFormula_active))
    def question_active(self):
        return '%s' %(bool(self.isQuestion_active))

    def subtopic_detail(self):
        return '%s %s %s %s %s' %(self.subTopic_name, bool(self.subTopic_isactive),bool(self.isTheory_active),bool(self.isFormula_active), bool(self.isQuestion_active))


class blogs(models.Model):
    subtopic=models.ManyToManyField(SubTopic)
    heading=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='static/images/blog_images',null=True)
    is_web_view=models.BooleanField(default=False)
    def get_subtopic(self):
        return '%s' %(self.subtopic)





# ebook models:
class Book(models.Model):
    title=models.CharField(max_length=200)
    number_of_pages=models.CharField(max_length=10, null=True)
    size=models.CharField(max_length=10, null=True)
    image=models.ImageField(upload_to='static/ebooks/images/',blank=True, null=True)
    isbn=models.CharField(max_length=10, null=True)


class link(models.Model):
    book=models.ForeignKey(Book, verbose_name='Book')
    link_text=models.CharField(max_length=1000)


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


class UserProfile(BaseModel):
    email = models.TextField(max_length=200)
    app_id = models.CharField(max_length=250, blank=True, null=True)
    app_version = models.CharField(max_length=10, blank=True, null=True)
    device_id = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.user.email +" "+self.app_id + " "+self.app_version

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
