# PWA-Django User Profile App
Simple Django app that manages user profiles

A simple django application with the following requirements:
- Python 3.6.9
- Django version 2.2.5
- Django PWA

This application is an MTV application whose sole purpore is to apply for a full time job at Avito.ma. The project demonstrates the ability to 
use MTV or MVC-like applications to handle Object Relational Mappers to abstract the use of an RDMS, and to focus only on the business logic of a web app.

The application has only one model for the moment: Profile. The model Profile has the following fields: name, email, and avatar. name is a character field
of 45 chars maximum. The email is an django EmailField, which is a special field that is already made in a way that it can only accept email 
address formats. The avatar is a FileField with a pre designated uploading path, that is also handled by Django.

The application has 2 endpoints: "/", and "/user/<pk>". The first one displays a list of profiles, and the second one displays a single profile,
with the ability to edit the contents. This latter is handling cleaning valid data, and serializing it to be compatible with the database used (sqlite in this case).

Here is an example of the first endpoint, the rest is fairly self-explanatory:
```python
def profiles(request):
    context = {
        'profiles': Profile.objects.all() # We define a context variable of a list of all Profile objects that we will then pass to the html file.
    }
    return render(request, "app/profiles.html", context) # The context variable is defined as a dictionary, and passed to a render function.
   ``` 
We can use special syntax inside our HTML to call functions and variables by using {{}} or {%%} tags. We use {{ example_var }} to use a variable
which was passed on through the context variable, and we use {%%} for functions and statements like {% if statement %} or {% for loop %}.

To make it easier for us to sanitize data through forms, we use ModelForms:
```python
class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email", "avatar"]
```
We can use EditUserForm to directly have users submit data through forms in HTML (with the use of the POST method, and a csrf token for protection).
This way we can skip the hassle of sanitizing data and focus more on the outcome of the function.

At last, we used ProgressiveWebApp to make the application ready for offline usage, using service workers, made with JavaScript.
The offline side of the application still has some few bugs, because this is my first time using PWA in a Django project. 

Here is my first attempt after some research online:
```javascript
var staticCacheName = "djangopwa-v1";

self.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll(["/base"]);
    })
  );
});

self.addEventListener("fetch", function(event) {
  var requestUrl = new URL(event.request.url);
  if (requestUrl.origin === location.origin) {
    if (requestUrl.pathname === "/") {
      event.respondWith(caches.match("/base"));
      return;
    }
  }
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
```

I took this opportunity, not only to apply for the job, but also to learn a new and very important feature.

More to come regardless of the outcome of this task.
