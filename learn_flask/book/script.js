const postData = {
    'c-intro': {
        title: "Introduction to C",
        body: "<p>C is a powerful general-purpose programming language...</p><p>It provides low-level access to memory and a clean syntax.</p>"
    },
    'py-intro': {
        title: "Introduction to Python",
        body: "<p>Python is an interpreted, high-level language...</p><p>Its design philosophy emphasizes code readability.</p>"
    }
};

function openBook() {
    document.getElementById('page-cover').classList.add('flipped');
}

function closeBook() {
    document.getElementById('page-cover').classList.remove('flipped');
}

function openPost(id) {
    const post = postData[id];
    document.getElementById('post-title').innerText = post.title;
    document.getElementById('post-body').innerHTML = post.body;
    document.getElementById('page-index').classList.add('flipped');
}

function closePost() {
    document.getElementById('page-index').classList.remove('flipped');
}