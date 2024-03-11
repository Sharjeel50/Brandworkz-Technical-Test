import { Outlet } from "react-router-dom";
import "./css/layout-page.css"; // Import your CSS file for additional styling

function Layout() {
  return (
    <div className="layout-container">
      <Outlet />
    </div>
  );
}

export default Layout;
