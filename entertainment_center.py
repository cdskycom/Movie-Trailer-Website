import media
import fresh_tomatoes

blade_runner = media.Movie("Blade Runner",
	"blade runner pursue and try to terminate replicants ",
	"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2501864539.webp",
	"http://vt1.doubanio.com/201805110033/b201987e0147bac60b14e0aa6d405989/view/movie/M/302200566.mp4")

coco = media.Movie("Coco",
	"A 12-year-old boy transported to the land of the dead accidentally",
	"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2503997609.webp",
	"http://vt1.doubanio.com/201805110038/c179249bd768e13e18887f2fb48afcfc/view/movie/M/302170862.mp4")

annihilation = media.Movie("Annihilation",
	"A sifi movie about future",
	"https://img1.doubanio.com/view/photo/m/public/p2516914607.webp",
	"http://vt1.doubanio.com/201805102321/8e953617965932411d9c5af7bcdce55a/view/movie/M/402290589.mp4")

black_panther = media.Movie("Black Panther",
	"A story of a superman",
	"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2512123434.webp",
	"http://vt1.doubanio.com/201805102321/05955405f5410512443c060e01f4320c/view/movie/M/302260827.mp4")

pacific_rim = media.Movie("Pacific Rim",
	"Giant machine fight with Giant machine",
	"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2512933684.webp",
	"http://vt1.doubanio.com/201805102322/f69884fea227df41e39e8a4f806c6539/view/movie/M/302280429.mp4")

wonder = media.Movie("Wonder",
	"A ugly boy's school life",
	"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2507709428.webp",
	"http://vt1.doubanio.com/201805102322/1388b3ca402a08bc116bbeca08a42542/view/movie/M/302250963.mp4")

movies = [blade_runner, coco, annihilation, black_panther, pacific_rim, wonder]
fresh_tomatoes.open_movies_page(movies)


