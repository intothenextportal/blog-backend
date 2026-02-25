import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import Sidebar from '../components/Sidebar'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function Home() {
  const [posts, setPosts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`${API_URL}/api/posts/`)
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  return (
    <main className="py-3 mb-3">
      <div className="container">
        <div className="row">
          <div className="col-md-9">
            {loading && <p>Loading posts...</p>}
            {posts.map((post) => (
              <div key={post.slug} className="card flex-md-row mb-4 border-light shadow-sm h-md-250">
                <img
                  className="card-img-left flex-auto d-none d-md-block"
                  height={250}
                  src={post.hero_image}
                  alt={post.hero_image_alt}
                />
                <div className="card-body d-flex flex-column align-items-start">
                  <h3 className="card-title mb-0">{post.title}</h3>
                  <Link to={`/blog/${post.slug}`} className="btn btn-outline-secondary mt-2">Read More</Link>
                </div>
              </div>
            ))}
          </div>
          <Sidebar />
        </div>
      </div>
    </main>
  )
}
