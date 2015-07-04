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
-- Name: shop_category; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE shop_category (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    slug character varying(50) NOT NULL,
    description text NOT NULL,
    is_active boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.shop_category OWNER TO postgres;

--
-- Name: shop_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE shop_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shop_category_id_seq OWNER TO postgres;

--
-- Name: shop_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE shop_category_id_seq OWNED BY shop_category.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY shop_category ALTER COLUMN id SET DEFAULT nextval('shop_category_id_seq'::regclass);


--
-- Data for Name: shop_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY shop_category (id, name, slug, description, is_active, created_at, updated_at) FROM stdin;
2	Accessories	accessories	Produk dengan kegunaan atau fungsi sebagai pelengkap bagi produk utama.	t	2013-08-22 10:30:22.816274+07	2014-01-23 12:46:37.576747+07
3	Consulting service	consulting-service	Produk yang berlaku sebagai imbal atas jasa konsultasi yang diberikan.	t	2013-08-22 10:32:13.182315+07	2014-01-23 12:48:07.680505+07
1	Food	food	Makanan dan atau yang terkait dengan kuliner.	t	2013-08-19 22:18:57.968674+07	2014-01-23 12:50:28.99209+07
4	3D Model Plan	3d-model-plan	3D Model Plan, kategori untuk perencana model 3 dimensi, seperti rumah pribadi dll.	t	2014-05-12 17:01:02.091145+07	2014-08-04 15:27:13.48229+07
\.


--
-- Name: shop_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('shop_category_id_seq', 4, true);


--
-- Name: shop_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_category
    ADD CONSTRAINT shop_category_pkey PRIMARY KEY (id);


--
-- Name: shop_category_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_category
    ADD CONSTRAINT shop_category_slug_key UNIQUE (slug);


--
-- Name: shop_category_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX shop_category_slug_like ON shop_category USING btree (slug varchar_pattern_ops);


--
-- Name: shop_category; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE shop_category FROM PUBLIC;
REVOKE ALL ON TABLE shop_category FROM postgres;
GRANT ALL ON TABLE shop_category TO postgres;
GRANT ALL ON TABLE shop_category TO toko WITH GRANT OPTION;


--
-- PostgreSQL database dump complete
--

