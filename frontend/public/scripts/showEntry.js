var entries;
var shownIdx;

// Retrives all the data as a javascript object.
// The data was given as a JSONstring from the app.
function loadEntries(JSONstr) {
    let txt = document.createElement("textarea");
    txt.innerHTML = JSONstr;
    entries = JSON.parse(txt.value).entries;
}

function uploadRate(idx) {
    let likes = document.getElementById("likes");
    likes.innerHTML = "&nbsp;" + entries[idx].likes;
    let dislikes = document.getElementById("dislikes");
    dislikes.innerHTML = "&nbsp;" + entries[idx].dislikes;
    let likesButton = document.getElementById("likesButton");
    let dislikesButton = document.getElementById("dislikesButton");
    let castedVote = entries[idx].hasOwnProperty("vote");
    if (castedVote && entries[idx].vote !== "dislike") {
        likesButton.disabled = true;
        likes.style = "color: green";
    } else {
        likesButton.disabled = false;
        likes.removeAttribute("style");
    }
    if (castedVote && entries[idx].vote !== "like") {
        dislikesButton.disabled = true;
        dislikes.style = "color: red";
    } else {
        dislikesButton.disabled = false;
        dislikes.removeAttribute("style");
    }
}

function uploadEntry(idx) {
    document.getElementById("video")
        .src = "https://www.youtube.com/embed/" + entries[idx].video  + "?&autoplay=1&mute=1&rel=0&showinfo=0";

    uploadRate(idx);
    
    document.getElementById("entryId")
        .value = entries[idx].id;

    document.getElementById("comment")
        .innerHTML = entries[idx].comment;

    document.getElementById("previousButton")
        .disabled = idx === 0;
    document.getElementById("nextButton")
        .disabled = idx === entries.length -1;
    
    shownIdx = idx;
}

function changeEntry(change) {
    uploadEntry(shownIdx + change);
}
