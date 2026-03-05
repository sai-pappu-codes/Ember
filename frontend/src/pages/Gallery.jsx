import React, { useState, useEffect } from 'react';
import './Gallery.css';

function Gallery() {
  const [galleryData, setGalleryData] = useState(null);
  const [selectedImage, setSelectedImage] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchGallery();
  }, []);

  const fetchGallery = async () => {
    try {
      const response = await fetch('/api/gallery');
      const data = await response.json();
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

  // Local images for gallery - all 14 images
  const localImages = [
    { id: 1, url: '/images/gallery-cafe-interior.webp', caption: 'Elegant Dining Room' },
    { id: 2, url: '/images/home-cafe-fausse.webp', caption: 'Restaurant Exterior' },
    { id: 3, url: '/images/gallery-ribeye-steak.webp', caption: 'Signature Ribeye Steak' },
    { id: 4, url: '/images/salmon-dish.jpg', caption: 'Grilled Salmon' },
    { id: 5, url: '/images/caprese-salad.jpg', caption: 'Fresh Caprese Salad' },
    { id: 6, url: '/images/tiramisu.jpg', caption: 'Classic Tiramisu' },
    { id: 7, url: '/images/dessert-closeup.jpg', caption: 'Exquisite Desserts' },
    { id: 8, url: '/images/cocktail-bar.jpg', caption: 'Signature Cocktails' },
    { id: 9, url: '/images/espresso-coffee.jpg', caption: 'Premium Espresso' },
    { id: 10, url: '/images/wine-cellar.jpg', caption: 'Wine Collection' },
    { id: 11, url: '/images/bar-interior.jpg', caption: 'Our Premium Bar' },
    { id: 12, url: '/images/elegant-table.jpg', caption: 'Fine Dining Setup' },
    { id: 13, url: '/images/chef-hands.jpg', caption: 'Culinary Artistry' },
    { id: 14, url: '/images/gallery-special-event.webp', caption: 'Private Events' }
  ];

  return (
    <div className="gallery-page">
      <div className="page-hero">
        <h1>Gallery</h1>
        <p>A Visual Journey Through Café Fausse</p>
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
                "Exceptional ambiance and unforgettable flavors. Café Fausse delivers 
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