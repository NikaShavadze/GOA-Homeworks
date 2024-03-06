 #შევქმნათ სია საყვარელი კინოების ან სერიალების, რომელსაც შევინახავთ ცვლადში. საბოლოოდ გამოვიტანოთ სია.
movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Godfather",
    "The Dark Knight",
    "Forrest Gump",
    "Pulp Fiction",
    "Interstellar",
    "The Matrix",
    "Schindler's List",
    "Eternal Sunshine of the Spotless Mind"
]

print(movies)

# სიიდან დავბეჭდოთ ერთი კონკრეტული მნიშვნელობა index-ით
print(movies[3])

#   შევქმნათ მეორე ცვლადი, რომლის სახელი იქნება საყვარელი კინო და მის მნიშვნელობას
# წინა სიიდან წამოვიღებთ
favourite_movie = movies[2]
print(favourite_movie)

#   მასივიდან ბოლო ელემენტი უარყოფითი index-ით წამოიღეთ. ასევე გამოიტანეთ ბოლოდან 
# მეორე ელემენტი, ისევ მინუსიანი ინდექსით
print(movies[-1])
print(movies[-2])

#   მომხმარებელს შევეკითხოთ საყვარელი მანქანის ბრენდი, რომელსაც შევინახავთ ცვლადში. შემდეგ 
# ეს ცვლადი ჩასვით სიაში და გამოვიტანოთ print-ით, მაგ: print([brand_variable_name_here])
user_input = input("Enter your favourite car brand: ")

car = [user_input]

print(car)