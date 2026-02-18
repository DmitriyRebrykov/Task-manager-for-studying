document.addEventListener("DOMContentLoaded", function ()
{
        document.querySelectorAll(".task-list").forEach(function (taskList) {
            Sortable.create(taskList, {
                handle: ".bi-arrow-down-up",
                animation: 150,
                filter: ".task-done",
                preventOnFilter: true,
                onEnd: function () {
                    const items = taskList.querySelectorAll(".task-item");
                    const order = Array.from(items)
                        .filter(el => !el.classList.contains("task-done"))
                        .map(el => ({ id: el.dataset.id }));

                    fetch("{% url 'main:task-reorder' %}", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": "{{ csrf_token }}",
                        },
                        body: JSON.stringify(order),
                    })
                    .then(r => r.json())
                    .then(data => console.log("Response:", data))
                    .catch(err => console.error("Error:", err));
                }
            });
        });
});
