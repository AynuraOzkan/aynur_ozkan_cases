from locust import HttpUser, task, between

class N11StressTestUser(HttpUser):
    wait_time = between(0.5, 1.5)  # Extensive testing with very short waiting times.

    def on_start(self):
        self.client.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Cookie": "c_ver=false; __hapc=be6c89b4-5e05-4341-b792-dd7a0e650794; 39667dd8108757fc657221e4a78cecef=539ce61a2620a9ca84f3279d9d23bd12; _cfuvid=PvZcXodXVzr7kmxBoCJCgw1OWodhKMKWxOpRFZN28_I-1774875769.2906187-1.0.1.1-a.3z4R9N_6a.1qH4qge8tuoZgjvEO1fYsjl_2T3wBRg; __hausc=03681659-cd6e-45b6-9a6c-63a1e38aa682; _ATHENA_DID=be6c89b4-5e05-4341-b792-dd7a0e650794; _wbauid=7302154391774875790; __dn_a=H4sIAAAAAAAACgXBQQ5DIQgFwLu8tSTiB0Vvg6BJF1112fTunfnihYVrxrG7UXefJNwu%2BeVGyWzZVdT4oCCxsE8Pm1tIT1WSR5j2mI0yh9fTtY4pKAgsoOCDhfB97zEm1ukkOow8zkM73WxkXo1AwRuLf39A%2FHIxjwAAAA%3D%3D; historyKey=%5B%7B%22link%22%3A%22%2Farama%3Fq%3Dfiltre%2Bkahve%22%2C%22keyword%22%3A%22filtre%20kahve%22%7D%2C%7B%22link%22%3A%22%2Farama%3Fq%3Dkahve%22%2C%22keyword%22%3A%22kahve%22%7D%2C%7B%22link%22%3A%22%2Farama%3Fq%3Dtelefon%22%2C%22keyword%22%3A%22telefon%22%7D%5D; __dn_v=H4sIAAAAAAAACpVSW2%2FaMBT%2BL%2Bd1pnLI3W%2BbBAUBFV3pOjRNUeI4qSE4ru1wadX%2FPjmOENOe9nSu3%2FHnc74PKIFAwSKapEUwChkOR4EfeKMiTsejsoxzzKIQx2kACCgQsEYY53QSiIfAOKPrA5BfvxGY2tncKCAfnwiaI7ceSBf2vgaCERR20CcCAwTbRn3tg67k%2F0OtFSanZsEujppk6sC15q0AYlTHEBiV0z0X9fqfCm07YdQANPzA3lvBgMD9avMF%2BwRjQNDkou7y2qaNAgR5eWTKcM1FPS%2BHteRKcaZsKLqmQWDaPRPDVOtuLpK58MSKp67QVHFpeiIOwIVhtcptyn1k9%2FoWxenDa1utnqffq10bqLj1w%2Fslrc3jmvuLWTU7z%2FX77lIUk22nJZ%2FGb%2Bq8nEXrJoqC1kxPXiazJtt%2Bbdg201mTndjLt200SdKH9WYifm7wKcgp9emLr3IZTh6XKzadp6Z7mvbARnlLutid9%2F2npfzBlL5hrMv9NQPju%2FGdF8LNhcf47xt7cRwkcRinHk76ex%2FloKnmeFvGSRIiMEcKxEdgNAUSITgNU4ft7h1y2L65DM%2F04ik4dfriprdUKiCgWNVpBghEH5asyrvG2NPJ29cjz5FrSweuWjuyvrbEvjcO0hgBdfUDt3q3CHl0Cqcu8weNMpaRXQMAAA%3D%3D; __dn_s=H4sIAAAAAAAACj3NSWoDMRSE4bvUWnJLbqk1QMhZNDzhQE%2Bx5DTG%2BO7BC%2FXuoyj4X6jwSCGWQlZyqV3gShvLQ6KRxxysNTkXnRIYMjwiTcm6qLgmobkaleTRuCvP2QRBkxbGKTAE%2BPUxzww53U7WLnrA49baXv0wHMdxWaW8pG0Zwj0s4fv3q9FMZVvBcP9cwVAbvDRGWaONE05PDHROTl61EIqhwEuGtOy9lNbWuXTUravRqSc82nOnn0%2F0L8GP73%2F9f%2BzIHAEAAA%3D%3D; _ATHENA_SID=c0ecce2c-c0ec-4617-bf4d-f2c34bddfc3b; ADRUM=s~1774892870913&r~aHR0cHMlM0ElMkYlMkZ3d3cubjExLmNvbSUyRmFyYW1hJTNGaGFzaCUzRDE5ODM3ODU3NTk=; __cf_bm=mUKDwBeKHPpmCrbH7_bX1aGHA8080horuqG35vtFZUc-1774892870.8412678-1.0.1.1-vh9MaHhKcLuRBMgYAY5rPbwo7gkrbl2uYj9g7Ua6maGb.8xv62_aAs9pbjXNmZ14iWcgI88zjE_A_J20GvT0.e3p.CVjsIU041Z.hbdmd5SzkFOG.MxkoegRe2MrlwKY; connect.sid=s%3AtA0qo6Lmh-L6_Xs1HhwEFc3v7DLTBILc.hNXLWK1eQ55KCYM4y2mg2xs1EtoRZMYsk7%2BI%2BXHbSTo; citrix_ns_id=AAE7SLfKaTvnSHs9AAAAADta2UAs0IoTFqmDO6b39oFOnjab0QYJOeRCzbQXuLXEOw==dLjKaQ==BEio7qhT8f0dje8BDWmz3jbTbPo=; _ATHENA_SID_TIMEOUT=1774894672654; cto_bundle=rxGASF9rWFhvQXJqbm5USSUyRm1FSm9oNWVubE5CRXFOTU9ud3R5dkRIdSUyRmVIZGhzMENNSzNwdWNyY3I4UEY1SkZocnEzSU9qWW5VM1lycUJCTk9LcklQell2TjIwYldZRmJFNTNOZ1hrd2Eyb0ZQM0ppM3RMckhDbjcxQXMwVWtLQmZtd2JZeWpyQ1BTdzYlMkJIRnl6VE8lMkZ2YmRNQSUzRCUzRA; clientType=Mobileweb",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        })

    @task
    def homepage_and_search(self):
        # Load homepage
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Ana sayfa yüklenemedi! Status: {response.status_code}")

        # search tests
        search_terms = ["telefon", "laptop", "ayakkabı", "kamera", "tablet", "çanta"]
        for term in search_terms:
            with self.client.get(f"/arama?q={term}", catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Arama başarısız: {term} Status: {response.status_code}")

        # results page navigation
        for page in range(1, 3):  # Test the first 2 pages.
            with self.client.get(f"/arama?q=telefon&pg={page}", catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Sonuç sayfası {page} yüklenemedi!")