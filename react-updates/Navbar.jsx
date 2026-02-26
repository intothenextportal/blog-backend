import { useState, useEffect } from 'react'
import { Link, useLocation } from 'react-router-dom'

const LOGO_URL =
  'https://static-cdn.jtvnw.net/jtv_user_pictures/8d4346c8-3f87-41e1-8f7e-0c3aede5b85f-profile_image-70x70.png'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false)
  const [dropdownOpen, setDropdownOpen] = useState(false)
  const [posts, setPosts] = useState([])
  const location = useLocation()

  useEffect(() => {
    fetch(`${API_URL}/api/posts/`)
      .then((res) => res.json())
      .then(setPosts)
      .catch(console.error)
  }, [])

  const isActive = (path) => location.pathname === path
  const isBlogActive = location.pathname.startsWith('/blog/')

  return (
    <header className="shadow-sm">
      <div className="shadow-sm rounded">
        <img className="d-block mx-auto" src={LOGO_URL} width="100" draggable="false" alt="Logo" />
      </div>

      <nav className="navbar navbar-expand-lg navbar-dark">
        <div className="container">
          <Link className="navbar-brand mr-5" to="/">Nicolas Garlinski</Link>
          <button className="navbar-toggler" type="button" onClick={() => setMenuOpen(!menuOpen)} aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className={`collapse navbar-collapse ${menuOpen ? 'show' : ''}`}>
            <ul className="navbar-nav mr-auto">
              <li className={`nav-item ${isActive('/') ? 'active' : ''}`}>
                <Link className="nav-link" to="/" onClick={() => setMenuOpen(false)}>Home</Link>
              </li>
              <li className={`nav-item ${isActive('/about') ? 'active' : ''}`}>
                <Link className="nav-link" to="/about" onClick={() => setMenuOpen(false)}>About me</Link>
              </li>

              <li className={`nav-item dropdown ${isBlogActive ? 'active' : ''}`}>
                <a className="nav-link dropdown-toggle" onClick={() => setDropdownOpen(!dropdownOpen)}
                  style={{ cursor: 'pointer' }} aria-haspopup="true" aria-expanded={dropdownOpen}>
                  Blog
                </a>
                <div className={`dropdown-menu ${dropdownOpen ? 'show' : ''}`} id="custom-dropdown-menu">
                  {posts.map((post) => (
                    <Link
                      key={post.slug}
                      className={`dropdown-item ${isActive(`/blog/${post.slug}`) ? 'active' : ''}`}
                      to={`/blog/${post.slug}`}
                      onClick={() => { setDropdownOpen(false); setMenuOpen(false) }}
                    >
                      {post.nav_label}
                      {post.is_new && <span className="badge badge-secondary badge-info ml-2">New</span>}
                    </Link>
                  ))}
                </div>
              </li>

              <li className={`nav-item ${isActive('/contact') ? 'active' : ''}`}>
                <Link className="nav-link" to="/contact" onClick={() => setMenuOpen(false)}>Contact</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  )
}
