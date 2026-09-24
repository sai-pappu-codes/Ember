import React, { useState, useEffect } from 'react';
import './Gallery.css';
import api from '../services/api';

function Gallery() {
  const [galleryData, setGalleryData] = useState(null);
  const [selectedImage, setSelectedImage] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchGallery();
  }, []);

  const fetchGallery = async () => {
    try {
      const { data } = await api.get('/gallery');
      setGalleryData(data);
    } catch (error) {
      console.error('Error fetching gallery:', error);
    } finally {
      setLoading(false);
    }
  };

  const openLightbox = (image) => {
    setSelectedImage(image);
  };

  const closeLightbox = () => {
    setSelectedImage(null);
  };

  if (loading) {
    return <div className="spinner"></div>;
  }

  // Local images for gallery - now 21 images including new menu items
  const localImages = [
    { id: 1, url: '/images/gallery-cafe-interior.webp', caption: 'Elegant Dining Room' },
    { id: 2, url: '/images/home-embertable.webp', caption: 'Restaurant Exterior' },
    { id: 3, url: '/images/gallery-ribeye-steak.webp', caption: 'Signature Ribeye Steak' },
    { id: 4, url: '/images/salmon-dish.jpg', caption: 'Grilled Salmon' },
    { id: 5, url: '/images/caprese-salad.jpg', caption: 'Fresh Caprese Salad' },
    { id: 6, url: '/images/tiramisu.jpg', caption: 'Classic Tiramisu' },
    { id: 7, url: '/images/dessert-closeup.jpg', caption: 'Exquisite Desserts' },
    { id: 8, url: '/images/elegant-desserts.jpg', caption: 'Tiramisu & Cheesecake by Candlelight' },
    { id: 9, url: '/images/cocktail-bar.jpg', caption: 'Signature Cocktails' },
    { id: 10, url: '/images/espresso-coffee.jpg', caption: 'Premium Espresso' },
    { id: 11, url: '/images/wine-cellar.jpg', caption: 'Wine Collection' },
    { id: 12, url: '/images/bar-interior.jpg', caption: 'Our Premium Bar' },
    { id: 13, url: '/images/elegant-table.jpg', caption: 'Fine Dining Setup' },
    { id: 14, url: '/images/chef-hands.jpg', caption: 'Culinary Artistry' },
    { id: 15, url: '/images/gallery-special-event.webp', caption: 'Private Events' },
    { id: 16, url: '/images/cheesecake.png', caption: 'Creamy New York Cheesecake' },
    { id: 17, url: '/images/vegetable-risotto.png', caption: 'Wild Mushroom Risotto' },
    { id: 18, url: '/images/caesar-salad.png', caption: 'Classic Caesar Salad' },
    { id: 19, url: '/images/red-wine.png', caption: 'Selection of Fine Red Wines' },
    { id: 20, url: '/images/white-wine.png', caption: 'Crisp White Wine Collection' },
    { id: 21, url: '/images/craft-beer.png', caption: 'Local Craft Beer Selection' }
  ];

  return (
    <div className="gallery-page">
      <div className="page-hero">
        <h1>Gallery</h1>
        <p>A Visual Journey Through EmberTable</p>
      </div>

      <div className="container">
        <section className="gallery-section">
          <h2>Our Space</h2>
          <div className="gallery-grid">
            {localImages.map(image => (
              <div key={image.id} className="gallery-item" onClick={() => openLightbox(image)}>
                <img src={image.url} alt={image.caption} />
                <div className="gallery-overlay">
                  <p>{image.caption}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="awards-section">
          <h2>Awards & Recognition</h2>
          <div className="awards-grid">
            <div className="award-card">
              <div className="award-icon">🏆</div>
              <h3>Culinary Excellence Award</h3>
              <p className="award-year">2022</p>
            </div>
            <div className="award-card">
              <div className="award-icon">🏆</div>
              <h3>Restaurant of the Year</h3>
              <p className="award-year">2023</p>
            </div>
            <div className="award-card">
              <div className="award-icon">🏆</div>
              <h3>Best Fine Dining Experience</h3>
              <p className="award-year">2023</p>
              <p className="award-org">Foodie Magazine</p>
            </div>
          </div>
        </section>

        <section className="reviews-section">
          <h2>Guest Reviews</h2>
          <div className="reviews-grid">
            <div className="review-card">
              <div className="review-stars">⭐⭐⭐⭐⭐</div>
              <p className="review-text">
                "Exceptional ambiance and unforgettable flavors. EmberTable delivers
                an extraordinary dining experience every time."
              </p>
              <p className="review-author">- Gourmet Review</p>
            </div>
            <div className="review-card">
              <div className="review-stars">⭐⭐⭐⭐⭐</div>
              <p className="review-text">
                "A must-visit restaurant for food enthusiasts. The attention to detail
                and quality is unmatched in the DC area."
              </p>
              <p className="review-author">- The Daily Bite</p>
            </div>
          </div>
        </section>
      </div>

      {/* Lightbox */}
      {selectedImage && (
        <div className="lightbox" onClick={closeLightbox}>
          <div className="lightbox-content">
            <img src={selectedImage.url} alt={selectedImage.caption} />
            <p>{selectedImage.caption}</p>
            <button className="lightbox-close" onClick={closeLightbox}>×</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Gallery;
