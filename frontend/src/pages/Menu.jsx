import React, { useState, useEffect } from 'react';
import './Menu.css';
import api from '../services/api';

function Menu() {
  const [menuData, setMenuData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState('all');

  useEffect(() => {
    fetchMenu();
  }, []);

  const fetchMenu = async () => {
    try {
      const { data } = await api.get('/menu');
      setMenuData(data);
    } catch (error) {
      console.error('Error fetching menu:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="spinner"></div>;
  }

  const categories = ['all', 'starters', 'main_courses', 'desserts', 'beverages'];

  return (
    <div className="menu-page">
      <div className="page-hero">
        <h1>Our Menu</h1>
        <p>Exquisite dishes crafted with passion</p>
      </div>

      <div className="container">
        {/* Category Filter */}
        <div className="menu-filters">
          {categories.map(cat => (
            <button
              key={cat}
              className={`filter-btn ${activeCategory === cat ? 'active' : ''}`}
              onClick={() => setActiveCategory(cat)}
            >
              {cat.replace('_', ' ').charAt(0).toUpperCase() + cat.replace('_', ' ').slice(1)}
            </button>
          ))}
        </div>

        {/* Menu Items */}
        <div className="menu-sections">
          {menuData && Object.entries(menuData).map(([category, items]) => {
            if (activeCategory !== 'all' && category !== activeCategory) return null;
            
            return (
              <div key={category} className="menu-section">
                <h2 className="menu-category-title">
                  {category.replace('_', ' ').charAt(0).toUpperCase() + category.replace('_', ' ').slice(1)}
                </h2>
                <div className="menu-items">
                  {items.map(item => {
                    // Map specific dishes to their images
                    const dishImages = {
                      'Grilled Salmon': '/images/salmon-dish.jpg',
                      'Ribeye Steak': '/images/gallery-ribeye-steak.webp',
                      'Tiramisu': '/images/tiramisu.jpg',
                      'Bruschetta': '/images/caprese-salad.jpg',
                      'Espresso': '/images/espresso-coffee.jpg',
                      'Cheesecake': '/images/cheesecake.png',
                      'Vegetable Risotto': '/images/vegetable-risotto.png',
                      'Caesar Salad': '/images/caesar-salad.png',
                      'Red Wine (Glass)': '/images/red-wine.png',
                      'White Wine (Glass)': '/images/white-wine.png',
                      'Craft Beer': '/images/craft-beer.png'
                    };
                    
                    return (
                      <div key={item.id} className="menu-item">
                        {dishImages[item.name] && (
                          <img 
                            src={dishImages[item.name]} 
                            alt={item.name} 
                            className="menu-item-image"
                          />
                        )}
                        <div className="menu-item-content">
                          <div className="menu-item-header">
                            <h3 className="menu-item-name">{item.name}</h3>
                            <span className="menu-item-price">${item.price.toFixed(2)}</span>
                          </div>
                          <p className="menu-item-description">{item.description}</p>
                          {item.vegetarian && <span className="vegetarian-badge">🌱 Vegetarian</span>}
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default Menu;