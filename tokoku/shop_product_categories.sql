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
-- Name: shop_product_categories; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE shop_product_categories (
    id integer NOT NULL,
    product_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.shop_product_categories OWNER TO postgres;

--
-- Name: shop_product_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE shop_product_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shop_product_categories_id_seq OWNER TO postgres;

--
-- Name: shop_product_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE shop_product_categories_id_seq OWNED BY shop_product_categories.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY shop_product_categories ALTER COLUMN id SET DEFAULT nextval('shop_product_categories_id_seq'::regclass);


--
-- Data for Name: shop_product_categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY shop_product_categories (id, product_id, category_id) FROM stdin;
99	37	2
100	36	2
101	35	3
102	29	2
103	20	1
110	22	2
111	12	2
112	24	2
113	4	3
114	9	1
117	5	2
118	6	3
119	7	2
120	17	2
121	16	3
122	8	3
124	18	1
126	23	2
127	26	2
129	27	1
132	50	3
133	51	2
134	52	1
135	52	3
136	53	3
137	54	2
138	55	2
140	57	1
141	58	1
142	59	1
146	62	3
147	63	2
149	64	3
150	65	3
151	14	2
49	2	2
50	3	1
58	11	1
62	15	3
152	13	1
75	28	3
154	66	3
155	67	3
156	68	2
83	38	3
85	40	2
89	44	2
90	45	2
91	46	3
92	47	3
93	48	3
96	25	1
97	30	3
98	31	1
157	10	1
158	41	3
159	56	1
160	69	2
161	70	3
162	1	1
163	71	2
164	60	1
165	19	1
166	43	3
167	72	2
169	74	2
179	39	4
183	61	4
184	75	4
185	73	4
186	49	4
187	42	4
\.


--
-- Name: shop_product_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('shop_product_categories_id_seq', 187, true);


--
-- Name: shop_product_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_product_categories
    ADD CONSTRAINT shop_product_categories_pkey PRIMARY KEY (id);


--
-- Name: shop_product_categories_product_id_category_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY shop_product_categories
    ADD CONSTRAINT shop_product_categories_product_id_category_id_key UNIQUE (product_id, category_id);


--
-- Name: shop_product_categories_category_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX shop_product_categories_category_id ON shop_product_categories USING btree (category_id);


--
-- Name: shop_product_categories_product_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX shop_product_categories_product_id ON shop_product_categories USING btree (product_id);


--
-- Name: product_id_refs_id_e629ab17; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY shop_product_categories
    ADD CONSTRAINT product_id_refs_id_e629ab17 FOREIGN KEY (product_id) REFERENCES shop_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: shop_product_categories_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY shop_product_categories
    ADD CONSTRAINT shop_product_categories_category_id_fkey FOREIGN KEY (category_id) REFERENCES shop_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: shop_product_categories; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE shop_product_categories FROM PUBLIC;
REVOKE ALL ON TABLE shop_product_categories FROM postgres;
GRANT ALL ON TABLE shop_product_categories TO postgres;
GRANT ALL ON TABLE shop_product_categories TO toko WITH GRANT OPTION;


--
-- PostgreSQL database dump complete
--

