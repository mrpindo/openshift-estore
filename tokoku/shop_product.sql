--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: shop_product; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE shop_product (
    id integer NOT NULL,
    imgfile character varying(100) NOT NULL,
    imgthumb character varying(100),
    name character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    brand character varying(50) NOT NULL,
    sku character varying(50) NOT NULL,
    price numeric(9,2) NOT NULL,
    old_price numeric(9,2) NOT NULL,
    is_active boolean NOT NULL,
    is_bestseller boolean NOT NULL,
    is_featured boolean NOT NULL,
    quantity integer NOT NULL,
    description text NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    "clientImgAttrs" character varying(255) NOT NULL
);


ALTER TABLE public.shop_product OWNER TO postgres;

--
-- Name: shop_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE shop_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shop_product_id_seq OWNER TO postgres;

--
-- Name: shop_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE shop_product_id_seq OWNED BY shop_product.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY shop_product ALTER COLUMN id SET DEFAULT nextval('shop_product_id_seq'::regclass);


--
-- Data for Name: shop_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY shop_product (id, imgfile, imgthumb, name, slug, brand, sku, price, old_price, is_active, is_bestseller, is_featured, quantity, description, created_at, updated_at, "clientImgAttrs") FROM stdin;
2	products/main/12_1.jpg	products/thumbnails/12_thumbnail.jpg	Nasi goreng pete	nasi-goreng-pete	CLK	CL32	60000.00	0.00	t	f	f	100	Click-on	2013-08-18 13:22:04.632+07	2013-08-22 10:31:04.677+07	
3	products/main/Hydrangeas.jpg	products/thumbnails/Hydrangeas_thumbnail.jpg	Mangga Gedong	mangga-gedong	FRUIT	FRT	15000.00	0.00	t	f	f	100	A good combination of natural fruit, with layering scent of sweet and sour.	2013-08-18 13:22:04.632+07	2014-01-15 21:08:25.922+07	
11	products/main/gambar_gta_san_andreas_zombotech.jpg	products/thumbnails/gambar_gta_san_andreas_zombotech_thumbnail.jpg	Mi goreng 	mi-goreng	MGR	WE2	23000.00	0.00	t	f	f	100	Mi goreng yang sangat nikmat -- dengan paket spesial hari Jumat.	2013-08-18 13:22:04.632+07	2014-01-15 21:35:43.943+07	
15	products/main/4.jpg	products/thumbnails/4_thumbnail.jpg	Consulting	consulting	CS	CS23	34000.00	0.00	t	f	f	100	Consulting service	2013-08-18 13:22:04.632+07	2013-08-22 10:33:00.216+07	
25	products/main/2_1.jpg	products/thumbnails/2_thumbnail.jpg	Gulai paku	gulai-paku	KopSus	AS3PEP	23000.00	0.00	t	f	f	100	Nice taste of KopSus	2013-08-18 13:22:04.632+07	2014-01-17 14:05:39.237506+07	{"x1":"60","y1":"3","x2":"264","y2":"236","w":"204","h":"233","imgw":"356","imgh":"241"}
22	products/main/47.jpg	products/thumbnails/47.jpg	Brownies	brownies	BRW	HJ6	70000.00	0.00	t	f	f	100	Nice Brownies	2013-08-18 13:22:04.632+07	2014-01-19 18:02:43.027616+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
12	products/main/53.jpg	products/thumbnails/53.jpg	Dendeng batokok	dendeng-batokok	DBT	78YU	130000.00	0.00	t	f	f	100	Dendeng batokok lamak bana, khas tengkareng PekanBaru	2013-08-18 13:22:04.632+07	2014-01-19 18:04:46.167532+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
4	products/main/7.jpg	products/thumbnails/7.jpg	Lamang Tapai	lamang-tapai	LTP	78UI	60000.00	0.00	t	f	f	100	Lamang tapai tapi lauik.	2013-08-18 13:22:04.632+07	2014-01-19 18:06:23.231744+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
19	products/main/bromo4.jpg	products/thumbnails/bromo4_thumbnail.jpg	Bromo View	bromo-view	LonKar	SKU	20000.00	0.00	t	f	f	100	Magnificent Bromo at Sunrise.	2013-08-18 13:22:04.632+07	2014-01-28 13:08:37.374168+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
6	products/main/35.jpg	products/thumbnails/35.jpg	Rakik kacang angek-angek	rakik-kacang-angek-angek	RKC	67Y	25000.00	0.00	t	f	f	100	Rakik kacang angek-angek dimasak pasir nan nikmat..	2013-08-18 13:22:04.632+07	2014-01-19 18:12:39.975541+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
17	products/main/45.jpg	products/thumbnails/45.jpg	Ayam Goreng Tepung	ayam-goreng-tepung	AYT	78YY	60000.00	0.00	t	f	f	100	Ayam goreng tepung dengan racikan khusus untuk lidah penikmat kuliner tradisional.	2013-08-18 13:22:04.632+07	2014-01-19 18:14:23.989807+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
8	products/main/46.jpg	products/thumbnails/46.jpg	Nasi kapau	nasi-kapau	NK	78YY	46000.00	0.00	t	f	f	100	Nasi kapau khas kapau Agam, enak bisa direkomen untuk pasangan.\r\n	2013-08-18 13:22:04.632+07	2014-01-19 18:16:09.3819+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
27	products/main/31.jpg	products/thumbnails/31_thumbnail.jpg	Barang baru	barang-baru	BRD	345D	34000.00	0.00	t	f	f	100	Suling bambu, kekuatan pada nada tingginya.	2013-08-18 13:22:04.632+07	2014-01-19 18:35:56.234881+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
14	products/main/40.jpg	products/thumbnails/40.jpg	Ulat Sutra	ulat-sutra	GT	GT$	60000.00	0.00	t	f	f	100	Ulat sutra alami, di peternakan desa daerah Sukabumi	2013-08-18 13:22:04.632+07	2014-01-22 18:21:31.717319+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
10	products/main/12.jpg	products/thumbnails/12_thumbnail.jpg	Shopping Bag	shopping-bag	TPC	TP21	125000.00	0.00	t	f	f	100	Shopping bag for E-Commerce. easier to use than average shopping bag.	2013-08-18 13:22:04.632+07	2014-01-22 21:13:54.211338+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
1	products/main/1.jpg	products/thumbnails/1.jpg	Rendang Juga	rendang-juga	RDB	U67	200000.00	0.00	t	f	f	100	Rendang sabana-bana rendang.	2013-08-18 13:22:04.632+07	2014-01-26 12:11:46.873906+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
37	products/main/Penguins.jpg	products/thumbnails/Penguins_thumbnail.jpg	Penguins	penguins	PENG	SKUPENG	23000.00	0.00	t	f	f	200	Nice Penguins have my great day..	2014-01-15 19:42:17.825+07	2014-01-17 14:09:36.1939+07	{"x1":"117","y1":"14","x2":"338","y2":"267","w":"221","h":"253","imgw":"356","imgh":"267"}
38	products/main/bromo4.jpg	products/thumbnails/bromo4_thumbnail.jpg	Great Bromo	great-bromo	LOC	GH5	230000.00	0.00	t	f	f	120	Great magnificent Bromo, breathtaking view and wonderful landscape	2014-01-15 22:35:25.04+07	2014-01-15 22:35:25.04+07	
42	products/main/tangga_spiral.png	products/thumbnails/tangga_spiral_thumbnail.png	Tangga spiral	tangga-spiral	TDh	45RG	630000.00	0.00	t	f	f	12	Tangga spiral, disain tepat untuk menghemat ruang di rumah tipe minimalis. 	2014-01-17 13:46:13.393415+07	2014-06-12 16:55:33.274487+07	{"x1":"84","y1":"0","x2":"259","y2":"200","w":"175","h":"200","imgw":"356","imgh":"200"}
40	products/main/Hydrangeas.jpg	products/thumbnails/Hydrangeas_thumbnail.jpg	Hydrangeas Color	hydrangeas-color	HyC	67TY	243000.00	0.00	t	f	f	120	Beautiful flower which emit energy to sorrounding area. Positive experience.	2014-01-17 13:43:28.94623+07	2014-01-17 13:43:28.946358+07	{"x1":"106","y1":"46","x2":"253","y2":"214","w":"147","h":"168","imgw":"356","imgh":"267"}
41	products/main/Desert.jpg	products/thumbnails/Desert_thumbnail.jpg	Rock Tip	rock-tip	RcT	23TT	200000.00	0.00	t	f	f	230	Tip of rock Mountain, somewhere in US. nice view though.	2014-01-17 13:45:08.092095+07	2014-01-22 21:25:53.055324+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
44	products/main/Jellyfish.jpg	products/thumbnails/Jellyfish_thumbnail.jpg	Tail JellyFish	tail-jellyfish	TJF	56TY	23000.00	0.00	t	f	f	234	Tail of Jelly Fish, very much sought in black market, and secondary marker. 	2014-01-17 13:49:47.552973+07	2014-01-17 13:49:47.553288+07	{"x1":"177","y1":"54","x2":"356","y2":"258","w":"179","h":"204","imgw":"356","imgh":"267"}
35	products/main/Chrysanthemum.jpg	products/thumbnails/Chrysanthemum_thumbnail.jpg	Chrysantemum	chrysantemum	CHT	SKU	21000.00	0.00	t	f	f	200	Nice flower in your heart	2014-01-15 19:02:42.752+07	2014-01-17 14:11:09.570601+07	{"x1":"177","y1":"0","x2":"356","y2":"204","w":"179","h":"204","imgw":"356","imgh":"267"}
39	products/main/dobel_dek_bed.png	products/thumbnails/dobel_dek_bed_thumbnail.png	Dobel dek bed	dobel-dek-bed	Private	67YT	1200000.00	0.00	t	f	f	2	Dobel dek bed. pilihan bed menarik untuk anak pre-teen, bagi keluarga kecil dan sedang. 	2014-01-17 13:36:53.467995+07	2014-06-08 12:11:23.901773+07	{"x1":"86","y1":"0","x2":"261","y2":"200","w":"175","h":"200","imgw":"356","imgh":"200"}
45	products/main/Koala.jpg	products/thumbnails/Koala_thumbnail.jpg	Koala Ear	koala-ear	KLE	78YT	23000.00	0.00	t	f	f	123	Koala ear, beautifully attached, colored/	2014-01-17 13:53:20.091221+07	2014-01-17 13:53:20.091355+07	{"x1":"235","y1":"5","x2":"356","y2":"143","w":"121","h":"138","imgw":"356","imgh":"267"}
31	products/main/Tulips.jpg	products/thumbnails/Tulips_thumbnail.jpg	Tulips	tulips	DJU	SKU	23000.00	0.00	t	f	f	100	Yes	2014-01-15 18:39:14.503+07	2014-01-17 14:08:36.803225+07	{"x1":"81","y1":"7","x2":"260","y2":"212","w":"179","h":"205","imgw":"356","imgh":"267"}
28	products/main/bromo4.jpg	products/thumbnails/bromo4_thumbnail.jpg	Mount Bromo	product-baru	BRM	78YT	32000.00	0.00	t	f	f	100	Gunung Bromo, the Magnificent, to resolve image upload folder issue.	2013-08-18 13:22:04.632+07	2014-01-15 21:11:45.071+07	
20	products/main/Hydrangeas.jpg	products/thumbnails/Hydrangeas_thumbnail.jpg	Pisang keju	pisang-keju	PKJ	34FT	15000.00	0.00	t	f	f	100	Nice and tender at first bite, try it!	2013-08-18 13:22:04.632+07	2014-01-17 14:12:55.006633+07	{"x1":"223","y1":"0","x2":"356","y2":"152","w":"133","h":"152","imgw":"356","imgh":"267"}
24	products/main/50.jpg	products/thumbnails/50.jpg	Salak pondoh	salak-pondoh	SLP	23dv	20000.00	0.00	t	f	f	100	Salak pondoh khas Jogja, spesial buat yang lagi kangen.	2013-08-18 13:22:04.632+07	2014-01-19 18:05:33.848059+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
9	products/main/45.jpg	products/thumbnails/45.jpg	Martabak mesir Kubang	martabak-mesir-kubang	MK	UI7	43000.00	0.00	t	f	f	100	Martabak Mesir kubang, spesial buat cuaca dingin	2013-08-18 13:22:04.632+07	2014-01-19 18:07:53.428759+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
5	products/main/13.jpg	products/thumbnails/13.jpg	Gudeg Jogja	gudeg-jogja	GJ	UI78	26000.00	0.00	t	f	f	100	Gudeg Jogja khas mataraman, enak nikmat tiada banding	2013-08-18 13:22:04.632+07	2014-01-19 18:11:45.427994+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
7	products/main/25.jpg	products/thumbnails/25.jpg	Es tebak Kasihan ombak	es-tebak-kasihan-ombak	ETB	hj67	25000.00	0.00	t	f	f	100	Es tebak khas Padang, sejuk dan segar dinikmati pas musim panas.	2013-08-18 13:22:04.632+07	2014-01-19 18:13:36.327763+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
16	products/main/39.jpg	products/thumbnails/39.jpg	Sala Lauak	sala-lauak	SL	78YU	12000.00	0.00	t	f	f	100	Yang ini pastinya khas Pariaman, enak dan gurih. Mantaaaaap.	2013-08-18 13:22:04.632+07	2014-01-19 18:15:06.231171+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
26	products/main/djangopony.jpg	products/thumbnails/djangopony.jpg	Django pony juga	django-pony-juga	HJT	123DS	120000.00	0.00	t	f	f	100	Django pony logo, as a merry go round Django framework logo. Nice one and have one!	2013-08-18 13:22:04.632+07	2014-01-19 18:33:49.033818+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
50	products/main/Desert.jpg	products/thumbnails/Desert_thumbnail.jpg	High Sand	high-sand	HES	JK67	23000.00	0.00	t	f	f	140	High end sand with style="display: none; " within the form tag, it works as expected!	2014-01-17 19:37:51.383759+07	2014-01-20 10:35:08.63846+07	{"x1":"161","y1":"47","x2":"254","y2":"153","w":"93","h":"106","imgw":"356","imgh":"267"}
51	products/main/Penguins.jpg	products/thumbnails/Penguins_thumbnail.jpg	Happy Feet	happy-feet	HPF	YU67	25000.00	0.00	t	f	f	213	Happy feet will make your day, filled with happiness. Buy one get two.	2014-01-17 19:59:30.439623+07	2014-01-20 10:36:38.96617+07	{"x1":"205","y1":"23","x2":"356","y2":"195","w":"151","h":"172","imgw":"356","imgh":"267"}
54	products/main/Chrysanthemum.jpg	products/thumbnails/Chrysanthemum_thumbnail.jpg	Bunga Chrysant	bunga-chrysant	BC	YU76	34000.00	0.00	t	f	f	128	Bunga merah menyala, cocok ditempatkan di ruang tamu...	2014-01-19 12:53:37.980741+07	2014-01-20 10:39:07.359746+07	{"x1":"54","y1":"44","x2":"233","y2":"249","w":"179","h":"205","imgw":"356","imgh":"267"}
55	products/main/Koala.jpg	products/thumbnails/Koala_thumbnail.jpg	Hidung Koala	hidung-koala	HK	89YU	234000.00	0.00	t	f	f	120	Hidung Koala, dngin dan lembut, cocok untuk penyayang peliharaan profesional.	2014-01-19 18:31:30.264112+07	2014-01-20 10:39:56.072005+07	{"x1":"125","y1":"124","x2":"221","y2":"234","w":"96","h":"110","imgw":"356","imgh":"267"}
57	products/main/MainCourse.jpg	products/thumbnails/MainCourse_thumbnail.jpg	Makan Besar	makan-besar	MKB	76UJ	340000.00	0.00	t	f	f	230	Makan besar, sekali seminggu bersama keluarga tercinta. Nikmat dan legaa..	2014-01-22 17:57:17.971891+07	2014-01-22 17:57:17.972084+07	{"x1":"83","y1":"0","x2":"316","y2":"267","w":"233","h":"267","imgw":"356","imgh":"267"}
58	products/main/TatiangMasakanPadang.jpg	products/thumbnails/TatiangMasakanPadang_thumbnail.jpg	Tatiang	tatiang	TT	JK7	243000.00	0.00	t	f	f	23	Tatiang manatiang, khas Sumatera barat. 	2014-01-22 17:58:35.961884+07	2014-01-22 17:58:35.962008+07	{"x1":"44","y1":"0","x2":"355","y2":"356","w":"311","h":"356","imgw":"356","imgh":"356"}
59	products/main/Appetizers.jpg	products/thumbnails/Appetizers_thumbnail.jpg	Sate Padang	sate-padang	STP	67YU	23000.00	0.00	t	f	f	24	Sate Padang khas Pariaman, dengan kegurihan tiada tara. Nikmati sekarang dan dapatkan diskon 50 untuk minggu depan.	2014-01-22 18:00:00.216159+07	2014-01-22 18:00:00.216401+07	{"x1":"100","y1":"10","x2":"254","y2":"187","w":"154","h":"177","imgw":"356","imgh":"187"}
62	products/main/1_1.jpg	products/thumbnails/1_thumbnail.jpg	Chef Suggest	chef-suggest	CS	78YU	240000.00	0.00	t	f	f	23	Chef suggestion for today. Might be good for you.	2014-01-22 18:05:55.077173+07	2014-01-22 18:05:55.077353+07	{"x1":"0","y1":"36","x2":"179","y2":"241","w":"179","h":"205","imgw":"356","imgh":"241"}
47	products/main/Lighthouse.jpg	products/thumbnails/Lighthouse_thumbnail.jpg	The rock	the-rock	TRC	67YU	23000.00	0.00	t	f	f	2300	The rock part of Lighthouse,somewhere in Pacific ocean.	2014-01-17 13:55:18.163568+07	2014-01-17 13:55:18.163697+07	{"x1":"119","y1":"28","x2":"298","y2":"233","w":"179","h":"205","imgw":"356","imgh":"267"}
48	products/main/Chrysanthemum.jpg	products/thumbnails/Chrysanthemum_thumbnail.jpg	Bloom	bloom	BL	67TT	234000.00	0.00	t	f	f	100	Bloom of Chrysant. adapt easily to low light emission.	2014-01-17 13:56:19.659992+07	2014-01-17 13:56:19.660191+07	{"x1":"43","y1":"41","x2":"222","y2":"246","w":"179","h":"205","imgw":"356","imgh":"267"}
52	products/main/Lighthouse.jpg	products/thumbnails/Lighthouse_thumbnail.jpg	Lighthouse by the Sea	lighthouse-by-the-sea	LBS	78YU	234000.00	0.00	t	f	f	100	Lighthouse by the sea. with multi categories, see how it looks like in the template!	2014-01-18 13:49:44.549462+07	2014-01-20 10:37:24.861084+07	{"x1":"0","y1":"17","x2":"135","y2":"171","w":"135","h":"154","imgw":"356","imgh":"267"}
53	products/main/Hydrangeas.jpg	products/thumbnails/Hydrangeas_thumbnail.jpg	Nan Tacelak	nan-tacelak	NTC	78YU	24000.00	0.00	t	f	f	240	Nan tacelak suko diurang, na buruak gamang tapacik, bia diundua dek sapik pianggang.	2014-01-19 12:51:45.282+07	2014-01-20 10:38:26.402422+07	{"x1":"100","y1":"42","x2":"279","y2":"247","w":"179","h":"205","imgw":"356","imgh":"267"}
61	products/main/pintu_geserpng.png	products/thumbnails/pintu_geserpng_thumbnail.png	Pintu geser	pintu-geser	SSP	78YU	780000.00	0.00	t	f	f	24	Pintu geser elegan, dengan minimal kebisingan, cocok untuk ruang minimalis.	2014-01-22 18:04:00.823569+07	2014-06-09 10:23:07.988351+07	{"x1":"114","y1":"0","x2":"280","y2":"190","w":"166","h":"190","imgw":"356","imgh":"200"}
46	products/main/Lighthouse.jpg	products/thumbnails/Lighthouse_thumbnail.jpg	The Home	the-home	TH	TY56	245000.00	0.00	t	f	f	230	The home of Lighthouse, somewhere in Pacific ocean.	2014-01-17 13:54:17.260668+07	2014-01-17 13:54:17.260799+07	{"x1":"0","y1":"0","x2":"151","y2":"173","w":"151","h":"173","imgw":"356","imgh":"267"}
30	products/main/Lighthouse.jpg	products/thumbnails/Lighthouse_thumbnail.jpg	Lighthouse	lighthouse	Ndeso	JK67	2000.00	0.00	t	f	f	100	Lighthouse satu dua tiga empat lima enam tujuh delapan sembilan sepuluh sebelas duabelas tigabelas empatbelas	2014-01-12 13:23:35.866+07	2014-01-17 14:07:42.518782+07	{"x1":"0","y1":"0","x2":"233","y2":"267","w":"233","h":"267","imgw":"356","imgh":"267"}
29	products/main/Koala.jpg	products/thumbnails/Koala_thumbnail.jpg	Koala Namu	koala-namu	YesBRAND	YesSKU	2000.00	0.00	t	f	f	100	satu dua tiga empat lima enam tujuh delapan sembilan sepuluh sebelas duabelas tigabelas empatbelas	2014-01-12 13:21:50.758+07	2014-01-17 14:11:51.068465+07	{"x1":"108","y1":"47","x2":"287","y2":"252","w":"179","h":"205","imgw":"356","imgh":"267"}
18	products/main/Jellyfish.jpg	products/thumbnails/Jellyfish_thumbnail.jpg	Es Teler	es-teler	ST	ST12	12000.00	0.00	t	f	f	100	Es Teler enak sekali..	2013-08-18 13:22:04.632+07	2014-01-19 18:28:59.027295+07	{"x1":"36","y1":"36","x2":"215","y2":"241","w":"179","h":"205","imgw":"356","imgh":"267"}
49	products/main/patung-kuda.png	products/thumbnails/patung-kuda_thumbnail.png	Patung kuda	patung-kuda	FT	67TY	230000.00	0.00	t	f	f	6	Disaing patung kuda, a DIY for advanced pro.	2014-01-17 13:57:33.567589+07	2014-06-11 11:59:54.385142+07	{"x1":"78","y1":"0","x2":"253","y2":"200","w":"175","h":"200","imgw":"356","imgh":"200"}
63	products/main/pool.jpg	products/thumbnails/pool_thumbnail.jpg	Cat Pool	cat-pool	CTP	YU67	234000.00	0.00	t	f	f	12	Cat by the pool side. Nice implementation of shyness and calm. Good vibration for your daly hectic life.	2014-01-22 18:11:27.385666+07	2014-01-22 18:11:27.385799+07	{"x1":"126","y1":"0","x2":"356","y2":"262","w":"230","h":"262","imgw":"356","imgh":"263"}
65	products/main/AfertheRain.png	products/thumbnails/AfertheRain_thumbnail.png	Gnome After	gnome-after	GN	67TT	340000.00	0.00	t	f	f	6	Gnome After the Rain. Cool and uncomplicated experience.	2014-01-22 18:19:30.907419+07	2014-01-22 18:19:30.90755+07	{"x1":"177","y1":"62","x2":"356","y2":"266","w":"179","h":"204","imgw":"356","imgh":"267"}
13	products/main/Lighthouse.jpg	products/thumbnails/Lighthouse_thumbnail.jpg	Ayam tulang lunak	ayam-tulang-lunak	ATL	TG45	45000.00	0.00	f	f	f	100	Ayam tulang lunak, makannya di pinggir pantai karang.	2013-08-18 13:22:04.632+07	2014-01-22 18:22:29.857564+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
67	products/main/sunset_at_kuta.jpg	products/thumbnails/sunset_at_kuta_thumbnail.jpg	Kuta Sunset	kuta-sunset	KTS	Jk67	650000.00	0.00	t	f	f	12	Kuta Sunset, beautiful view, enchanted landscape.	2014-01-22 19:23:35.832763+07	2014-01-22 19:23:35.832931+07	{"x1":"53","y1":"62","x2":"232","y2":"267","w":"179","h":"205","imgw":"356","imgh":"267"}
68	products/main/j0231293.jpg	products/thumbnails/j0231293_thumbnail.jpg	Dam Sketch	dam-sketch	DMS	HG5	54000.00	0.00	t	f	f	23	Dam Sketch. Located at the land of nowhere.	2014-01-22 19:27:59.758825+07	2014-01-22 19:27:59.759044+07	{"x1":"49","y1":"0","x2":"318","y2":"308","w":"269","h":"308","imgw":"356","imgh":"308"}
56	products/main/Default.jpg	products/thumbnails/Default_thumbnail.jpg	Makan Puas	makan-puas	MKP	78PK	245000.00	0.00	t	f	f	120	Makan puas dengan pilihan menu bervariasi, luangkan waktu anda untuk menikmati sajian kulinar khar Padang.	2014-01-22 17:56:02.059247+07	2014-01-23 12:36:12.202921+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
69	products/main/Tulips.jpg	products/thumbnails/Tulips_thumbnail.jpg	Tulip Tip	tulip-tip	TT	UI67	23000.00	0.00	t	f	f	67	Tulip tip only, with additional red color request.	2014-01-23 12:38:03.702415+07	2014-01-23 12:38:03.702599+07	{"x1":"142","y1":"20","x2":"212","y2":"100","w":"70","h":"80","imgw":"356","imgh":"267"}
70	products/main/intraweb.png	products/thumbnails/intraweb_thumbnail.png	IntWeb	intweb	ITW	87Y	800000.00	0.00	t	f	f	898	Just a test product.	2014-01-23 15:41:39.294861+07	2014-01-23 15:41:39.294992+07	{"x1":"100","y1":"10","x2":"279","y2":"215","w":"179","h":"205","imgw":"356","imgh":"277"}
60	products/main/3.jpg	products/thumbnails/3_thumbnail.jpg	Lontong Sayur Lamak Rasonyo	lontong-sayur-lamak-rasonyo	LTS	UI67	12000.00	0.00	t	f	f	23	Lontong sayur nikmat, dengan serpihan kerupuk merah.	2014-01-22 18:01:40.080903+07	2014-01-28 12:01:14.241425+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
74	products/main/medic_clear.jpg	products/thumbnails/medic_clear_thumbnail.jpg	ToolMedic	toolmedic	TM	98	390000.00	0.00	t	f	f	20	Medical Tool	2014-04-20 22:54:36.268924+07	2014-04-20 22:54:36.269176+07	{"x1":"95","y1":"0","x2":"301","y2":"236","w":"206","h":"236","imgw":"356","imgh":"236"}
36	products/main/Desert.jpg	products/thumbnails/Desert_thumbnail.jpg	Desert	desert	BR	SKU	12000.00	0.00	t	f	f	210	Desert Storm	2014-01-15 19:21:00.983+07	2014-01-17 14:10:36.8059+07	{"x1":"40","y1":"10","x2":"219","y2":"215","w":"179","h":"205","imgw":"356","imgh":"267"}
73	products/main/meja_belajar.png	products/thumbnails/meja_belajar_thumbnail.png	Meja belajar	meja-belajar	Private	62fr4	634000.00	0.00	t	f	f	4	Meja belajar ukuran sedang, dengan bahan terbaik. cocok untuk anak sekolah.	2014-02-01 10:35:22.730472+07	2014-06-09 11:03:21.785245+07	{"x1":"96","y1":"6","x2":"262","y2":"196","w":"166","h":"190","imgw":"356","imgh":"200"}
43	products/main/Jellyfish.jpg	products/thumbnails/Jellyfish_thumbnail.jpg	Head Jelly	head-jelly	HDD	56TR	245000.00	0.00	t	f	f	230	Head of JellyFish , poisonous creature in tropical sea. Bright color	2014-01-17 13:48:43.420643+07	2014-01-28 13:42:14.503423+07	{"x1":"","y1":"","x2":"","y2":"","w":"","h":"","imgw":"","imgh":""}
71	products/main/Jellyfish.jpg	products/thumbnails/Jellyfish_thumbnail.jpg	Jellyfish Head	jellyfish-head	JFH	78H	87000.00	0.00	t	f	f	239	Nicely photographed sea creature. Rancak bana.	2014-01-26 13:31:39.369089+07	2014-01-26 13:31:39.369243+07	{"x1":"14","y1":"14","x2":"193","y2":"219","w":"179","h":"205","imgw":"356","imgh":"267"}
23	products/main/Chrysanthemum.jpg	products/thumbnails/Chrysanthemum_thumbnail.jpg	Baso Petis	baso-petis	BP	GH56	25000.00	0.00	t	f	f	100	Baso petis khas Jawa Timur, enak dinikmati pas musim hujan.	2013-08-18 13:22:04.632+07	2014-01-19 18:32:51.126309+07	{"x1":"0","y1":"0","x2":"179","y2":"205","w":"179","h":"205","imgw":"356","imgh":"267"}
64	products/main/Tabuik.jpg	products/thumbnails/Tabuik_thumbnail.jpg	Tabuik	tabuik	TB	45RT	340000.00	0.00	t	f	f	12	Tabuik, memperingati maulid nabi. Fascinating experience in the land of goddess.	2014-01-22 18:17:55.957719+07	2014-01-22 18:18:35.235551+07	{"x1":"53","y1":"0","x2":"260","y2":"237","w":"207","h":"237","imgw":"356","imgh":"237"}
66	products/main/Branch.png	products/thumbnails/Branch_thumbnail.png	Leaf Branch	leaf-branch	LfB	YU67	450000.00	0.00	t	f	f	12	Leaf Branch synthetic art, adapted from nature and give maximum relaxation 	2014-01-22 19:20:12.017543+07	2014-01-22 19:20:42.031146+07	{"x1":"161","y1":"0","x2":"356","y2":"222","w":"195","h":"222","imgw":"356","imgh":"223"}
72	products/main/Lighthouse_5.jpg	products/thumbnails/Lighthouse_thumbnail.jpg	Mercusuar	mercusuar	MRS	89YU	34000.00	0.00	t	f	f	23	Mercusuar, penerangan dalam kegelapan bagi kapal-kapal yang melintasi gugusan karang di pesisir pantai selatan Jawa.	2014-01-28 13:44:53.511315+07	2014-01-28 13:44:53.511448+07	{"x1":"0","y1":"0","x2":"179","y2":"205","w":"179","h":"205","imgw":"356","imgh":"267"}
75	products/main/Rumah2Lantai.png	products/thumbnails/Rumah2Lantai_thumbnail.png	Rumah 2 Lantai	rumah-2-lantai	Private	122	2300000.00	0.00	t	f	f	2	Rumah 2 Lantai, cocok untuk keluarga kecil berbahagia.\r\nLuas Bangunan: 200m2.\r\n\r\nhttp://127.0.0.1:8000/Rumah2Lantai/	2014-05-12 17:02:02.710052+07	2014-06-09 11:02:38.101334+07	{"x1":"76","y1":"0","x2":"251","y2":"200","w":"175","h":"200","imgw":"356","imgh":"200"}
\.


--
-- Name: shop_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('shop_product_id_seq', 75, true);


--
-- Name: shop_product_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_product
    ADD CONSTRAINT shop_product_name_key UNIQUE (name);


--
-- Name: shop_product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_product
    ADD CONSTRAINT shop_product_pkey PRIMARY KEY (id);


--
-- Name: shop_product_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_product
    ADD CONSTRAINT shop_product_slug_key UNIQUE (slug);


--
-- Name: shop_product_name_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX shop_product_name_like ON shop_product USING btree (name varchar_pattern_ops);


--
-- Name: shop_product_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX shop_product_slug_like ON shop_product USING btree (slug varchar_pattern_ops);


--
-- Name: shop_product; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE shop_product FROM PUBLIC;
REVOKE ALL ON TABLE shop_product FROM postgres;
GRANT ALL ON TABLE shop_product TO postgres;
GRANT ALL ON TABLE shop_product TO toko WITH GRANT OPTION;


--
-- Name: shop_product_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE shop_product_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE shop_product_id_seq FROM postgres;
GRANT ALL ON SEQUENCE shop_product_id_seq TO postgres;
GRANT SELECT,USAGE ON SEQUENCE shop_product_id_seq TO toko;


--
-- PostgreSQL database dump complete
--

