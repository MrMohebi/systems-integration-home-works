const BASE_URL = "http://127.0.0.1:6060"


const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
    // alert("کابر با موفقیت ساخته شد")
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});


const onCreateUser = () => {
    const name = document.getElementById("name").value;
    const lastName = document.getElementById("last-name").value;
    const phone = document.getElementById("phone").value;

    let topics = []

    if (document.getElementById("sports").checked) {
        topics.push("sports")
    }
    if (document.getElementById("tech").checked) {
        topics.push("tech")
    }
    if (document.getElementById("politics").checked) {
        topics.push("politics")
    }
    if (topics.length < 1) {
        alert("لطفا حداقل یک موضوع را انتخاب کنید")
        return
    }

    let apiData = {
        "name": name,
        "lastname": lastName,
        "phone": phone,
        "topics": topics.join(",")
    }

    fetch(BASE_URL + '/user/create', {
        method: 'POST',
         headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(apiData)
    }).then(res => {
        alert("کابر با موفقیت ساخته شد")
        document.getElementById("name").value = ""
        document.getElementById("last-name").value = ""
        document.getElementById("phone").value = ""
    }).catch(error => {
        alert('خطا در ارسال درخواست: ' + error)
    });
}


const onCreateNews = () => {
    const title = document.getElementById("title").value;
    const category = document.getElementById("category").value;
    const content = document.getElementById("content").value;
    console.log(category);
    let apiData = {
        "title": title,
        "text": content,
        "topic": category,
    }

    fetch(BASE_URL + '/admin/news/create', {
        method: 'POST',
         headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(apiData)
    }).then(res => {
        alert("خبر با موفقیت ساخته شد")
        document.getElementById("title").value = ""
        document.getElementById("content").value = ""
        document.getElementById("category").value = "sport"
    }).catch(error => {
        alert('خطا در ارسال درخواست: ' + error)
    });
}


