from flask import Flask,render_template # Flask la class phu trach chay sever
#routing la chia trang

app = Flask(__name__)
 

#function binding

@app.route("/") #/ LA TRANG CHU
def home() :     # 2 cau nay phai di vs nhau , neu ng dung truy cap vao trang chu , truy cap vao home
    return "he nho fo` nac"

@app.route("/c4e")
def c4e():
    return " he nho c4e,hihi"

@app.route("/me")
def me():
    return "ten em la Dao Trong Cuong , hay moi nguoi hay goi la Kira"

# @app.route("/hi/dung") # nhớ lấy phần http ở terminal để chạy trên webbrowser
# def dung():
#     return "ban ben canh em ten la Pham Anh Dung , dep zai vai lon` ma ban ay phu vai cax"

@app.route("/hi/<name>") 
def hi_name(name):
    return "ban ben canh em ten la " + name + ", dep zai vai lon` ma ban ay phu vai cax"

@app.route("/add/<a>/<b>") # hien tai o day a va b la dang string nen o? duoi s ms phai de int(a) con khong khai bao thang <int:a> va <int:b>
def sum(a,b):
    s= int(a) + int(b)
    return str(s)   #return trong route luon phai la string nen phai dat s = va return str(s) de chuyen so' s ve thanh string


# @app.route("/posts")
# def posts():
#     return "<h3>dua cai con tec</h3>" #return ngắn như thế này bt dùng để return báo lỗi not found chứ bt k để

@app.route("/posts/<int:index>") #de int:index vi neu k de int: thi index se la dang string
def posts(index):
    titles =[
        "hihihi",
        "hahahha",
        "huhuhu"
    ]
    t= titles[index]
    content =[
        " Úi zời ơi , bố mày lại sợ mày quá",
        "Úi zời ơi , bố mày sợ mày quá cơ",
        "a tha em , a kinh mày quá cơ"
    ]
    c = content[index]
    return render_template('post.html',title = t,content = c)

#dung cho movies.html
@app.route("/movies")
def movies():
    # movies_title =[
    #     "Chipucu",
    #     "Cuchipu",
    #     "Chicupu",
    #     "Puchicu",
    # ]
    # return render_template("movies.html",titles = movies_title )

    movie_list=[
        {
            "title": "kabuto",
            "image": "https://s3-ap-southeast-1.amazonaws.com/img.spiderum.com/sp-images/204ea740e57511e88d027b1a1d3bb425.jpg"
        },
        {
            "title": "ex-aid",
            "image": "https://s.pacn.ws/640/tn/kamen-rider-exaid-tv-series-insert-song-collection-533989.1.jpg?ovfo9h"
        }
    ]
    return render_template("movies.html",movies = movie_list )




@app.route("/movie")
def movie():
    return render_template("movie.html",name = "kamen rider kabuto final form", image = "http://1.bp.blogspot.com/_YF1tNfQVN8w/TPOw6tgNsVI/AAAAAAABpK8/90HlUsPL5_M/s1600/3.jpg") # render template se tu mo` vao` tat ca cac phan`

if __name__ == "__main__" :
    app.run(debug=True)         # setup xong 1 sever

    