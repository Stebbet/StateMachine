let first = true;
$(document).on('click', '.login_button', function () {
    $.ajax({
        type: 'GET',
        url: 'login',
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');//now its working
        },
        error: function (output) {
            alert("fail");
        }
    });
});

$(document).on('click', '.register_button', function () {
    $.ajax({
        type: 'GET',
        url: 'register',
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');//now its working
        },
        error: function (output) {
            alert("fail");
        }
    });
});


$(document).on('click', '.account_button', function () {
    $.ajax({
        type: 'GET',
        url: 'account_settings',
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');//now its working
        },
        error: function (output) {
            alert("fail");
        }
    });
});

$(document).on('click', '.about-btn', function () {
    $.ajax({
        type: 'GET',
        url: 'about',
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');//now its working
        },
        error: function (output) {
            alert("fail");
        }
    });
});


function checkLogin() {
    if (sessionStorage.getItem('loggingin') !== 'false' && sessionStorage.getItem('loggingin') !== null && document.getElementById('login_failed').value === "true") {
        $.ajax({
            type: 'GET',
            url: 'login_failed',
            success: function (output) {
                $('#modalcontainer').html(output).modal('show');//now its working
                sessionStorage.setItem('login_failed', 'false');
            },
            error: function (output) {
                alert("fail");
            }
        });
    } else if (sessionStorage.getItem('pass-reset') === 'true') {
        $.ajax({
            type: 'GET',
            url: 'login',
            success: function (output) {
                $('#modalcontainer').html(output).modal('show');//now its working
                sessionStorage.setItem('pass-reset', 'false');
            },
            error: function (output) {
                alert("fail");
            }
        });
    }


}

function checkRegister() {
    if (sessionStorage.getItem('loggingin') !== 'false' && sessionStorage.getItem('loggingin') !== null && document.getElementById('register_failed').value === "true") {
        $.ajax({
            type: 'GET',
            url: 'register_failed',
            success: function (output) {
                $('#modalcontainer').html(output).modal('show');//now its working
            },
            error: function (output) {
                alert("fail");
            }
        });
    }
}

function updateLogin() {
    sessionStorage.setItem('loggingin', JSON.stringify({'transitions': transitionDict, 'states': stateDict}));
}

let current_file = "";

function toDash() {
    $.ajax({
        type: 'GET',
        url: 'dashboard',
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');//now its working
        },
        error: function (output) {
            alert("fail");
        }
    });
}

$(document).on('click', '.help-btn', function () {
    $.ajax({
        type: 'GET',
        url: 'help',
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');//now its working
        },
        error: function (output) {
            alert("fail");
        }
    });
});


function save() {
    let title = document.getElementsByName('diagram-title').item(0).value;
    if (title === "") {
        title = "Untitled";
    }
    let image = layer.toDataURL({
        pixelRatio: 0.2
    })
    let content = {'transitions': transitionDict, 'states': stateDict};
    let json_data = `{"title": "${title}", "content": ${JSON.stringify(content)}, "image": "${image}"}`;

    $.ajax({
        type: 'POST',
        url: 'save/',
        data: json_data,
        success: function (e) {
            $.ajax({
                type: 'GET',
                url: 'save_success',
                success: function (output) {
                    $('#modalcontainer').html(output).modal('show');//now its working
                    current_file = title;
                },
                error: function (output) {
                    alert("fail");
                }
            });
        },

        error: function (e) {
            $.ajax({
                type: 'GET',
                url: 'account_error',
                success: function (output) {
                    $('#modalcontainer').html(output).modal('show');//now its working
                },
                error: function (output) {
                    alert("fail");
                }
            });
        }
    });
}

function save_frame() {


    let title = document.getElementsByName('diagram-title').item(0).value;
    if (title === "") {
        title = "Untitled";
    }


    $.ajax({
        type: 'GET',
        url: `get_user_diagrams`,
        success: function (output) {
            let user_diagrams = JSON.parse(output)['diagrams'];
            if (user_diagrams.includes(title) && title !== current_file) {
                $.ajax({
                    type: 'GET',
                    url: `file_already_exists`,
                    success: function (output) {
                        $('#modalcontainer').html(output).modal('show');
                    },
                    error: function (output) {
                        alert("fail");
                    },
                });
            } else {
                save();
            }

        },
        error: function (output) {
            $.ajax({
                type: 'GET',
                url: `account_error`,
                success: function (output) {
                    $('#modalcontainer').html(output).modal('show');
                },
                error: function (output) {
                    alert("fail");
                },
            });
        },
    });

}

function privacy_policy() {
    $.ajax({
        type: 'GET',
        url: `privacy_policy`,
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');
        },
        error: function (output) {
            alert("fail");
        },
    });
}

function toRegister() {
    $('#modalcontainer').hide();
    $.ajax({
        type: 'GET',
        url: `register`,
        success: function (output) {
            $('#modalcontainer').html(output).show();
        },
        error: function (output) {
            alert("fail");
        },
    });
}

function load_pass_reset() {
    $.ajax({
        type: 'GET',
        url: `password-reset`,
        success: function (output) {
            $('#modalcontainer').html(output).show();
        },
        error: function (output) {
            alert("fail");
        },
    });
}

function pass_reset_to_login() {
    window.location.href('/');
    $.ajax({
        type: 'GET',
        url: `login`,
        success: function (output) {
            $('#modalcontainer').html(output).show();
        },
        error: function (output) {
            alert("fail");
        },
    });
}

function toLogin() {
    $('#modalcontainer').hide();
    $.ajax({
        type: 'GET',
        url: `login`,
        success: function (output) {
            $('#modalcontainer').html(output).show();
        },
        error: function (output) {
            alert("fail");
        },
    });
}

function delete_account() {
    $.ajax({
        type: 'POST',
        url: 'delete_account',
        success: function (e) {
            $.ajax({
                type: 'GET',
                url: 'delete_success',
                success: function (output) {
                    window.location.reload();
                    $('#modalcontainer').html(output).modal('show');
                },
                error: function (output) {
                    alert("fail");
                }
            });
        },

        error: function (e) {
            alert('fail');
        }
    });
}

function imports() {
    $.ajax({
        type: 'GET',
        url: `imports`,
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');
        },
        error: function (output) {
            alert("fail");
        },
    });
}


$(document).on('click', '#delete-user', function () {
    $.ajax({
        type: 'GET',
        url: `are_you_sure`,
        success: function (output) {
            $('#modalcontainer').html(output).modal('show');
        },
        error: function () {
            alert("fail");
        },
    });
});

let deleting = false;

function deleteDiagram(card) {
    $.ajax({
        type: 'POST',
        url: `delete/${card.id}`,
        success: function (e) {
            $.ajax({
                type: 'GET',
                url: 'dashboard',
                success: function (output) {
                    $('#modalcontainer').html(output);
                    deleting = true;
                },
                error: function (output) {
                    alert("fail");
                }
            });
        },

        error: function (e) {
            alert("Failed to Delete");
        }
    });
}

function openMachine(card) {
    // Gets the value of the machine id after clicking the card
    if (!deleting) {
        $.ajax({
            type: 'GET',
            url: `get_diagram/${card.id}`,
            success: function (output) {
                $(function () {
                    $('#modalcontainer').modal('toggle');
                });
                let o = JSON.parse(output);
                current_file = o['title'];
                clearHistory();
                regenerate(o['content'], o['title']);
                update_history();
            },
            error: function (output) {
                alert("fail");
            }
        });
    }
    deleting = false;


}

$(document).ready(function () {
    function getCookie(c_name) {
        if (document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start, c_end));
            }
        }
        return "";
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });

});

