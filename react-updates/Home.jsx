import { Link } from 'react-router-dom'
import Sidebar from '../components/Sidebar'

const homePosts = [
  {
    title: 'Babylon 5',
    description: 'This is an article talking about the similarities and differences between Babylon 5 and Deep Space Nine',
    img: 'https://insidepulse.com/wp-content/uploads/2023/07/Babylon-5-banner-e1690152594533.jpg',
    imgWidth: 500,
    imgHeight: undefined,
    to: '/blog/spider-man',
  },
  {
    title: 'Deep Space Nine',
    description: 'An in-depth look at Star Trek: Deep Space Nine explores how the series redefined the Star Trek universe with its darker tone, serialized storytelling, and complex moral questions.',
    img: 'https://occ-0-8407-2218.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABR0mSrs9eCmlIxHDDQV0XbdtS9kldgVMXly_uiYddzMGZ2hVDIUpgnUQ21GqqiLJghnibEAVuADb5FAUfhPhbvancCr92GV6nu8d.jpg?r=6d9',
    imgWidth: undefined,
    imgHeight: 250,
    to: '/blog/batman',
  },
  {
    title: 'An American living in Poland',
    description: 'This article follows the journey of an American who traded the familiarity of home for a new life in Poland, exploring the cultural surprises, everyday challenges, and unexpected joys that come with living abroad.',
    img: 'https://www.census.gov/newsroom/stories/polish-american-heritage-month/_jcr_content/root/responsivegrid/responsivegrid_861367604/imagecore.coreimg.jpeg/1663958747371/stories-polish-american-1300x867.jpeg',
    imgWidth: undefined,
    imgHeight: 250,
    to: '/blog/panther',
  },
]

export default function Home() {
  return (
    <main className="py-3 mb-3">
      <div className="container">
        <div className="row">
          <div className="col-md-9">
            {homePosts.map((post) => (
              <div key={post.title} className="card flex-md-row mb-4 border-light shadow-sm h-md-250">
                <img
                  className="card-img-left flex-auto d-none d-md-block"
                  width={post.imgWidth}
                  height={post.imgHeight}
                  src={post.img}
                  alt={post.title}
                />
                <div className="card-body d-flex flex-column align-items-start">
                  <h3 className="card-title mb-0">{post.title}</h3>
                  <p className="card-text mb-auto">{post.description}</p>
                  <Link to={post.to} className="btn btn-outline-secondary">Read More</Link>
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
