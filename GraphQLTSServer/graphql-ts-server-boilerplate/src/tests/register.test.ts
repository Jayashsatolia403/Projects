import { startServer } from "..";

const email = "j@j.com"
const password = "fjjhfcka"

const mutation = `
mutation {
    register(email = "${email}", password: "${password}")
}
`;

test("Register User", async () => {
    await startServer();
});