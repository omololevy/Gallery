from django.test import TestCase
from .models import Image,Category,Location



class CategoryTestClass(TestCase):
    #setup method
    def setUp(self):
        self.category = Category(name='Technology')
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
        
    def test_save_method(self):
        self.category.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
       
    def test_update_category(self):
        self.category.save_category()
        new_name="Tech"
        self.category.update_category(self.category.id,new_name)
        update = Category.objects.get(name="Tech")
        self.assertEquals(update.name,"Tech")
        
        
class LocationTestClass(TestCase):
    #setup method
    def setUp(self):
        self.location = Location(name='Kisumu')
        self.location.save_location()
        
    def tearDown(self):
        Location.objects.all().delete()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
    def test_save_method(self):
        self.location.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
    
    def test_update_location(self):
        self.location.save_location()
        new_name="Malindi"
        self.location.update_location(self.location.id,new_name)
        update = Location.objects.get(name='Malindi')
        self.assertEquals(update.name,"Malindi")
        
    
        
class ImageTestClass(TestCase):
    #setup method
    def setUp(self):
        self.location = Location(name='Kisumu',)
        self.location.save_location()
        self.category = Category(name='Technology')
        self.category.save_category()
        self.new_image = Image(name='Veg',description="Awesome green vegetation" ,location=self.location, category=self.category)
        self.new_image.save_image()
        
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
    
    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        
    def test_save_image(self):
        self.new_image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image_name(self.new_image.id,'test')
        updated= Image.objects.get(name='test')
        self.assertEqual(updated.name,'test')
        
    def test_delete_image(self):
        self.new_image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)==0)
            
    def test_get_image_by_id(self):
        self.new_image.save_image()
        image_found=self.new_image.get_image_by_id(self.new_image.id)
        self.assertTrue(len(image_found)>0)
        
    def test_filter_by_location(self):
        self.new_image.save_image()
        found_images = self.new_image.filter_by_location(location='Kisumu')
        self.assertTrue(len(found_images) == 1)
        
    def test_search_image_by_category(self):
        self.new_image.save_image()
        found_img = self.new_image.search_by_category('Technology')
        self.assertTrue(len(found_img) == 1)


