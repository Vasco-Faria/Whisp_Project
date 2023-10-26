$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});
$(document).on("click", ".js-toggle-modal", function(e) {
    e.preventDefault()
    $(".js-modal").toggleClass("hidden")
})
.on("click", ".js-submit", function(e) {
    e.preventDefault()
    const text = $(".js-post-text").val().trim()
    const $btn = $(this)

    if(!text.length) {
        return false
    }

    $btn.prop("disabled", true).text("Posting!")
    $.ajax({
        type: 'POST',
        url: $(".js-post-text").data("post-url"),
        data: {
            text: text
        },
        success: (dataHtml) => {
            $(".js-modal").addClass("hidden");
            $("#posts-container").prepend(dataHtml);
            $btn.prop("disabled", false).text("New Post");
            location.reload();
            $(".js-post-text").val('')
        },
        error: (error) => {
            console.warn(error)
            $btn.prop("disabled", false).text("Error");
        }
    });
})
.on("click", ".js-follow", function(e) {
    e.preventDefault();
    const action = $(this).attr("data-action")

    $.ajax({
        type: 'POST',
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        success: (data) => {
            $(".js-follow-text").text(data.wording)
            if(action == "follow") {
                
                console.log("DEBUG", "unfollow")
                $(this).attr("data-action", "unfollow")
            } else {
                
                console.log("DEBUG", "follow")
                $(this).attr("data-action", "follow")
            }
        },
        error: (error) => {
            console.warn(error)
        }
    });
})

const videos = document.querySelectorAll('.auto-play-video');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.play(); 
        } else {
            entry.target.pause(); 
        }
    });
});

videos.forEach(video => {
    observer.observe(video);
});


function likePost(form) {
    const post_id = form.getAttribute('data-post-id');
    const likeButton = form.querySelector('button');
    const likeCount = likeButton.querySelector('strong span');

    $.post("{% url 'feed:likepost' %}", { post_id: post_id }, function(data) {
        if (data.liked) {
            likeButton.classList.remove('positive');
            likeButton.classList.add('negative');
            likeButton.innerHTML = "<strong>" + data.like_count + " <i class='bx bx-heart'></i></strong>";
        } else {
            likeButton.classList.remove('negative');
            likeButton.classList.add('positive');
            likeButton.innerHTML = "<strong>" + data.like_count + " <i class='bx bxs-heart'></i></strong>";
        }
    });
}

