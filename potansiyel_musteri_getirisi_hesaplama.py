###Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama###

##İş Problemi##
#Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
#oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
#ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

#Veri Seti Özellikleri#
#persona.csv
#PRICE – Müşterinin harcama tutarı
#SOURCE – Müşterinin bağlandığı cihaz türü
#SEX – Müşterinin cinsiyeti
#COUNTRY – Müşterinin ülkesi
#AGE – Müşterinin yaşı


#Görev 1:Soruları Yanıtlayınız
#Soru1
##persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
persona = pd.read_csv("persona.csv")
df = persona.copy()
df.head()
df.info()

#Soru2
##Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

#Soru3
##Kaç unique PRICE vardır?
df['PRICE'].nunique()

#Soru4
##Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

#Soru5
##Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()

#Soru6
##Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE": "sum"})

#Soru7
##SOURCE türlerine göre satış sayıları nedir?
df.groupby("SOURCE")["PRICE"].count()

#Soru8
##Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE": "mean"})

#Soru9
##SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE": "mean"})

#Soru10
##COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

#Görev2
##COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

#Görev3
##Çıktıyı PRICE’a göre sıralayınız.
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

#Görev4
##Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df = agg_df.reset_index()
agg_df.head()

#Görev5
##Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
agg_df["AGE"] = agg_df["AGE"].astype("category")
label = ["0_18", "19_23", "24_30", "31_40", "41_70"]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0,18,24,30,40,70], labels=label)
agg_df.head()

#Görev6
##Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df["customer_level_based"] = [str(i[0]).upper() + "_" + str(i[1]).upper() + "_" + str(i[2]).upper() + "_" + str(i[5]).upper() for i in agg_df[agg_df.columns].values]
agg_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"}).reset_index()
agg_df["customer_level_based"].value_counts()
agg_df.head()

#Görev7
##Yeni müşterileri (personaları) segmentlere ayırınız.
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

#Görev8
##Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customer_level_based"] == new_user]

new_user_two = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customer_level_based"] == new_user_two]