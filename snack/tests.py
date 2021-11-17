from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='ashrf@admin.com',
            email='ashrf@admin.com',
            password='0000'
        )

        self.post = Snack.objects.create(
            title='pancake',
            description='food',
            purchaser=self.user
        )

    
    def test_string_representation(self):
        post = Snack(title='title')
        self.assertEqual(str(post), post.title)


#####################
    def test_all_fields(self):
        
        self.assertEqual(str(self.post), 'pancake')
        self.assertEqual(f'{self.post.purchaser}', 'ashrf@admin.com')
        self.assertEqual(self.post.description, 'food')

   ###########################

    def test_blog_list_view(self):
        response = self.client.get(reverse('list_view'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_view(self):
        response = self.client.get(reverse('snack-detail', args='1'))
        self.assertEqual(response.status_code, 200)


        ####### 

        
    def test_blog_update_view(self):
        response = self.client.post(reverse('snack-update', args='1'), {
            'title': 'chips',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')

    ############

    def test_home_status(self):
        expected = 200
        url = reverse('list_view')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_template(self):
        url = reverse('list_view')
        response = self.client.get(url)
        actual = 'snack/list_view.html'
        self.assertTemplateUsed(response, actual)
    
#    ################

    def test_create_view(self):
        response = self.client.post(reverse('snack-create'), {
            'title': 'chips',
            'purchaser': self.user,
            'description' :'healthy food',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')
        self.assertContains(response, 'healthy food')
        self.assertContains(response, 'ashrf')

    def test_delete_view(self):
        response = self.client.get(reverse('snack-delete', args='1'))
        self.assertEqual(response.status_code, 200)
  



