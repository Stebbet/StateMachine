from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
import datetime

"""
Developer note:
When no field is explicitly defined as the primary key, Django automatically creates an auto-incrementing integer primary key.
This has been used for every model, and thus there are no explicitly stated primary keys
These primary keys can be referenced to with .pk if needed
"""


class UserInfo(models.Model):
    """This table holds additional data on each user

    Columns:
        user (OneToOneField): This is a link to an existing user in the auth_user table.
            Each user can only have ONE entry in UserInfo (OneToOne relation), and if the user is deleted, the CASCADE option ensures this
            record will also be deleted

    Functions:
        __str__(self): Defines how each record in the table is represented (E.g. 7 dev [CS=1 TP=1]) (AKA ID Username [currentStreak totalPoints])

    Other:
        Meta defines how information from this table is referred to in the admin screen (named for purpose of clarity)
    """
    objects = models.Manager()
    user = models.OneToOneField(
        User,
        help_text="Linking this information to the user in auth_User it relates to",
        on_delete=models.CASCADE,
    )

    class_id = models.IntegerField(
        default=None,
        help_text="Code for the classroom the user is in"
    )

    is_teacher = models.BooleanField(
        default=False,
        help_text="Boolean for if the user is a teacher or not"
    )

    def __str__(self):
        return str(self.user.__str__())

    class Meta:
        verbose_name_plural = "Additional User Info"
        verbose_name = "Users Info"


class DiagramsModel(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50,
        default="Untitled",
        help_text="Title of this FSM"
    )
    description = models.TextField(
        default="Untitled Diagram",
        max_length=500,
        help_text="User description of this FSM"
    )

    content = models.JSONField(
        default=dict,
        help_text="JSON Data Content of this FSM"
    )

    image = models.TextField(
        default="",
        help_text="Image of this FSM, to be displayed to the user in the dashboard"
    )

    date_created = models.DateTimeField(
        auto_now_add=True,  # Automatically updates when created
        help_text="Date this FSM is created"
    )
    date_modified = models.DateTimeField(
        auto_now=True,  # Automatically updates when modified
        help_text="Date this FSM is last modified"
    )

    def __str__(self):
        return "Diagram: " + str(self.title) + " - " + str(self.description)

    class Meta:
        verbose_name_plural = "Diagrams Model"
        verbose_name = "Diagrams"
