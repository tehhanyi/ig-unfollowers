document.getElementById('unfollowersForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const twoFactorCode = document.getElementById('twoFactorCode').value;

    const response = await fetch('/.netlify/functions/find_unfollowers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, twoFactorCode })
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});

document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/.netlify/functions/find_unfollowers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();

    if (result.error && result.error === "2FA code required") {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('twoFactorForm').style.display = 'block';
    } else {
        document.getElementById('result').innerText = JSON.stringify(result, null, 2);
    }
});

document.getElementById('twoFactorForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const twoFactorCode = document.getElementById('twoFactorCode').value;

    const response = await fetch('/.netlify/functions/find_unfollowers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, twoFactorCode })
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});