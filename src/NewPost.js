import { Outlet } from "react-router-dom"

export default function Posts() {
    return (
        <div>
            <h1>One Post</h1>
            <Outlet />
        </div>
    )
}
