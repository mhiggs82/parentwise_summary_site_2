import React from 'react';
import Link from '@docusaurus/Link';

export default function BookCard({ badge, title, author, insights, actions, to }) {
    return (
        <div className="pw-card" style={{ flex: '0 0 280px', display: 'flex', flexDirection: 'column' }}>
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '12px' }}>
                <span className="pw-badge" style={{ fontSize: '10px' }}>{badge}</span>
            </div>
            <div style={{
                height: '160px',
                background: 'rgba(255,255,255,0.05)',
                borderRadius: '8px',
                marginBottom: '16px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '40px'
            }}>
                📖
            </div>
            <h3 style={{ fontSize: '18px', margin: '0 0 4px 0', minHeight: '44px' }}>{title}</h3>
            <p className="text-tertiary" style={{ fontSize: '13px', margin: '0 0 16px 0' }}>{author}</p>

            <div style={{
                borderTop: '1px solid var(--pw-border)',
                paddingTop: '12px',
                marginTop: 'auto',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
            }}>
                <div style={{ display: 'flex', gap: '8px', fontSize: '13px' }}>
                    <span>💡 {insights}</span>
                    <span>✓ {actions}</span>
                </div>
                <Link to={to} style={{
                    color: 'var(--pw-purple)',
                    fontWeight: '600',
                    fontSize: '14px',
                    textDecoration: 'none'
                }}>
                    Read →
                </Link>
            </div>
        </div>
    );
}
