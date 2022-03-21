import datetime
from django.urls import reverse, reverse_lazy

from django.utils import timezone
from django.test import TestCase

from .models import Question

def create_question(statement:str, days_offset:int) -> Question:
    """ Creates a question given the statement and a days offset for the publication
    date in days """
    question = Question(
        statement=statement,
        publication_date = timezone.now() + datetime.timedelta(days=days_offset)
    )
    return question

class QuestionModelTest(TestCase):

    def test_was_pub_recently_with_future_questions(self):
        """ was_published__recently must return False for questions with
        publication_date in the future """
        future_time = timezone.now() + datetime.timedelta(days=9)
        future_question = Question(
            statement="¿Cuál es el mejor profesor de platzi?",
            publication_date=future_time
        )
        self.assertIs(future_question.was_published_recently(),False)

class ListViewTest(TestCase):

    def test_no_questions(self):
        """ If there are no questions registered, an appropiate message is shown"""
        response = self.client.get(reverse_lazy("polls:polls"))
        self.assertQuerysetEqual(response.context['question_list'],[])
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")

    def test_future_questions(self):
        """ If there are questions with publication_date in the future, they are 
        not shown in the list """
        question = create_question("¿Test question 0?", 2)
        question.save()
        response = self.client.get(reverse_lazy("polls:polls"))
        self.assertQuerysetEqual(response.context['question_list'],[])
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")

    def test_past_questions(self):
        """ If there are questions with publication_date in the past, they are 
        shown in the list """
        question = create_question("¿Test question 0?", -2)
        question.save()
        response = self.client.get(reverse_lazy("polls:polls"))
        self.assertTrue(len(response.context['question_list']) == 1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.statement)

class DetailsViewTest(TestCase):

    def test_future_question(self):
        """ The details view of a question with publication_date in the future
        returns a 404 error """
        question = create_question("¿Test question 0?", 2)
        question.save()
        response = self.client.get(reverse_lazy("polls:details",kwargs={"pk": question.id}))
        self.assertEqual(response.status_code, 404)
        self.assertNotIn("question",response.context)


    def test_past_question(self):
        """ The details view of a question with publication_date in the past
        is shown"""
        question = create_question("¿Test question 0?", -2)
        question.save()
        response = self.client.get(reverse_lazy("polls:details",kwargs={"pk": question.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.statement)