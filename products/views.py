from django.shortcuts import render

films = [
    {
        "id": 1,
        "title":"Immortals",
        "image_url":"https://www.impawards.com/2011/posters/immortals_ver3.jpg",
        "description":"Epic fantasy action about Hercules and the battle against the Titans.",
        "mark":8,
        "year":2011,
        "genre":"fantasy" 
    },
    {
        "id":2,
        "title": "Oz the Great and Powerful",
        "image_url": "https://www.impawards.com/2013/posters/oz_the_great_and_powerful.jpg",
        "description": "A magician is transported to the magical Land of Oz and becomes involved in a battle between good and evil witches.",
        "mark": 7,
        "year": 2013,
        "genre": "fantasy"
    },
    {
        "id":3,
        "title": "Pan's Labyrinth",
        "image_url": "https://www.impawards.com/2006/posters/pans_labyrinth.jpg",
        "description": "A dark fantasy tale where a young girl discovers a mysterious labyrinth filled with mythical creatures.",
        "mark": 9,
        "year": 2006,
        "genre": "fantasy"
    }
]

# Create your views here.
def index(request):
    return render(request, 'products/index.html', {'films': films})

def oneProductPage(request, id):
    return render(request, 'products/oneProductPage.html', {'film' : films[id-1]})