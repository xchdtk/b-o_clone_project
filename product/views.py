from django.views     import View
from django.http      import JsonResponse
from django.http      import HttpResponse

from product.models   import Category, Product, Main, SubCategory,ProductImage, Color, Inspiration,Feature, ProductSpecification


class ProductView(View):
    def get(self, request, category_id):
        color_list        = []
        image_list        = []
        products_list     = []
        
        products          = Product.objects.filter(sub_category__category_id = category_id).prefetch_related('product_images', 'color')
        
        for product in products:
            for color in set(product.color.all()):
                    color_list.append(color.name)
                    image_list.append(product.product_images.filter(color = color)[0].image_url)

            products_list.append({
                'id'           : product.id,
                'title'        : product.title,
                'detail_title' : product.detail_title,
                'price'        : product.price,
                'colors'        : color_list,
                'image_url'    : image_list 
                })
            color_list    = []
            image_list    = []
                
        return JsonResponse({"results" : products_list}, status = 200)

class SubcategoryProductView(View):
    def get(self, request, sub_category_id):
        products      = Product.objects.select_related('sub_category').filter(sub_category_id = sub_category_id)
        color_list    = []
        image_list    = []
        products_list = []

        for product in products:
            for color in set(product.color.all()):
                    color_list.append(color.name)
                    image_list.append(product.product_images.filter(color = color)[0].image_url)

            products_list.append({
                'id'           : product.id,
                'title'        : product.title,
                'detail_title' : product.detail_title,
                'price'        : product.price,
                'colors'       : color_list,
                'image_url'    : image_list    
                })
            color_list    = []
            image_list    = []
        return JsonResponse({"results" : products_list}, status = 200)

class ProductDetailView(View):
    def get(self, request, product_id):
        
        product_list        = []
        product             = Product.objects.get(id = product_id)
        colors              = []
       
        image_list          = []

        for color in set(product.color.all()):
            image_list = [product.image_url for product in product.product_images.filter(color = color)]
                 
            colors.append(
                    {
                        "color_id"   : color.id,
                        "color_name" : color.name,
                        'image'      : image_list
                    }
                )

        inspiration    = Inspiration.objects.get(product=product)
        features       = Feature.objects.get(product=product)
        specifications_list = []

        for specification in product.specifications.all():
            data = ProductSpecification.objects.get(product = product, specifications = specification)
            specifications_list.append(data.data)
         
        product_list.append(
             {
                'productsData' : {
                    'id'           : product_id,
                    'title'        : product.title,
                    'detailTitle'  : product.detail_title,
                    'description'  : product.description,
                    'price'        : product.price,
                    'colors'        : colors
                },

                'inspirations'  : {
                    'id'           : inspiration.id,
                    'title'        : inspiration.title["title"],
                    'description'  : inspiration.description["description"],
                    'video'        : inspiration.video_url["video_url"],
                    'slide_image'  : inspiration.slide_image_url['image_url']
                },    

                'features' : {
                    'id'          : features.id,
                    'title'       : features.title["title"],
                    'sub_title'   : features.subtitle["subtitle"],
                    'description' : features.description["description"],
                    'images'      : features.image_url["image_url"]
                },

                'specifications' : specifications_list
                
            
            }
        )

        return JsonResponse({"results" : product_list}, status = 200)


         

        










        