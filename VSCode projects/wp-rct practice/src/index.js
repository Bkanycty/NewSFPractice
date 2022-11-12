import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Calculator from "./components/Calculator";
import App from "./components/App";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
      },
    {
        path: '/calculator',
        element: <Calculator />
    },
  ]
);

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
);