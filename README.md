django-test
===========

Commands

- New Project - `django-admin.py startproject djangotest`
- Start server - `./manage.py runserver 0.0.0.0:8000`
- Setup initial DB based on apps in settings.py - `./manage.py syncdb`
- Urls
  - http://127.0.0.1:8000/
  - http://127.0.0.1:8000/admin
- Istall dir

```
python -c "
import sys
sys.path = sys.path[1:]
import django
print(django.__path__)"
```

- Defualt Templates at - `django/contrib/admin/templates`

Links

- Settings.py - https://docs.djangoproject.com/en/1.6/topics/settings/
- Manage/Admin - https://docs.djangoproject.com/en/1.6/ref/django-admin/
- urls.py - https://docs.djangoproject.com/en/1.6/topics/http/urls/
- wsgi - https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
- DB Ref - https://docs.djangoproject.com/en/1.6/topics/db/queries/
- Templates - https://docs.djangoproject.com/en/1.6/ref/templates/api/#template-loaders


Tutorials

> https://docs.djangoproject.com/en/1.6/intro/tutorial01/
> https://docs.djangoproject.com/en/1.6/intro/tutorial02/
> https://docs.djangoproject.com/en/1.6/intro/tutorial03/

- New App - `python manage.py startapp polls`
- Syncdb  SQL view - `python manage.py sql polls` produces

```
BEGIN;
CREATE TABLE "polls_poll" (
    "id" integer NOT NULL PRIMARY KEY,
    "question" varchar(200) NOT NULL,
    "pub_date" datetime NOT NULL
);
CREATE TABLE "polls_choice" (
    "id" integer NOT NULL PRIMARY KEY,
    "poll_id" integer NOT NULL REFERENCES "polls_poll" ("id"),
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
COMMIT;
```

- Sync db again - `./manage.py syncdb`
- Use the shell - `python manage.py shell` (setups environment in addition to >python )

```
>>> from polls.models import Poll, Choice

# Make sure our __unicode__() addition worked.
>>> Poll.objects.all()
[<Poll: What's up?>]

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Poll.objects.filter(id=1)
[<Poll: What's up?>]
>>> Poll.objects.filter(question__startswith='What')
[<Poll: What's up?>]

# Get the poll that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Poll.objects.get(pub_date__year=current_year)
<Poll: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Poll.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Poll matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Poll.objects.get(id=1).
>>> Poll.objects.get(pk=1)
<Poll: What's up?>

# Make sure our custom method worked.
>>> p = Poll.objects.get(pk=1)
>>> p.was_published_recently()
True

# Give the Poll a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a poll's choices) which can be accessed via the API.
>>> p = Poll.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> p.choice_set.all()
[]

# Create three choices.
>>> p.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> p.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = p.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Poll objects.
>>> c.poll
<Poll: What's up?>

# And vice versa: Poll objects get access to Choice objects.
>>> p.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> p.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any poll whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(poll__pub_date__year=current_year)
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

# Let's delete one of the choices. Use delete() for that.
>>> c = p.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```



