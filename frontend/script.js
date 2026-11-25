
const API_URL = "http://127.0.0.1:8000";

// Add student
document.getElementById("studentForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const student = {
        name: document.getElementById("name").value,
        register_number: document.getElementById("register_number").value,
        email: document.getElementById("email").value,
        department: document.getElementById("department").value
    };

    const params = new URLSearchParams(student);

    try {
        const response = await fetch(
            `${API_URL}/students?${params.toString()}`,
            { method: "POST" }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Failed to add student");
        }

        alert(result.message);

        document.getElementById("studentForm").reset();

        loadStudents();

    } catch (error) {
        alert("Error: " + error.message);
    }
});


// Display students
async function loadStudents() {

    try {
        const response = await fetch(`${API_URL}/students`);

        if (!response.ok) {
            throw new Error("Unable to load students");
        }

        const students = await response.json();

        const table = document.getElementById("studentTable");

        table.innerHTML = "";

        students.forEach(student => {

            const row = document.createElement("tr");

            [
                student.id,
                student.name,
                student.register_number,
                student.email,
                student.department
            ].forEach(value => {
                const cell = document.createElement("td");
                cell.textContent = value;
                row.appendChild(cell);
            });

            table.appendChild(row);
        });

    } catch (error) {
        console.error("Error loading students:", error);
    }
}


// Load students when website opens
loadStudents();
