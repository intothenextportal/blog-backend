import { useParams, Navigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import Sidebar from '../components/Sidebar'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function BlogPost() {
  const { slug } = useParams()
  const [post, setPost] = useState(null)
  const [loading, setLoading] = useState(true)
  const [notFound, setNotFound] = useState(false)

  useEffect(() => {
    fetch(`${API_URL}/api/posts/${slug}/`)
      .then((res) => {
        if (res.status === 404) { setNotFound(true); return null }
        return res.json()
      })
      .then((data) => { if (data) setPost(data) })
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [slug])

  if (notFound) return <Navigate to="/" replace />

  if (loading) return (
    <main className="py-3 mb-3">
      <div className="container">
        <p>Loading...</p>
      </div>
    </main>
  )

  if (!post) return null

  const renderContent = (item, idx) => {
    switch (item.type) {
      case 'lead':
        return <p key={idx} className="lead">{item.text}</p>
      case 'text':
        return <p key={idx}>{item.text}</p>
      case 'image':
        return <img key={idx} src={item.image_url} className="img-fluid rounded mb-3" alt={item.image_alt} />
      case 'blockquote':
        return (
          <blockquote key={idx} className="blockquote">
            <p className="mb-0">{item.text}</p>
            <strong className="blockquote-footer">{item.blockquote_footer}</strong>
          </blockquote>
        )
      default:
        return null
    }
  }

  return (
    <main className="py-3 mb-3">
      <div className="container">
        <div className="row">
          <div className="col-md-9">
            <h2>{post.title}</h2>
            <p className="lead">by <a href="#">{post.author}</a></p>
            <p>Posted on {new Date(post.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</p>
            <img src={post.hero_image} className="img-fluid rounded mb-3" alt={post.hero_image_alt} />
            {post.content.map((item, idx) => renderContent(item, idx))}
          </div>
          <Sidebar />
        </div>
      </div>
    </main>
  )
}
