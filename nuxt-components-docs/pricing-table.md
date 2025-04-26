<!-- source: https://ui.nuxt.com/components/pricing-table --> # PricingTablePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PricingTable.vue)

A responsive pricing table component that displays tiered pricing plans with
feature comparisons.

## Usage

The PricingTable component provides a responsive and customizable way to
display pricing plans in a table format, automatically switching between a
horizontal table layout on desktop for easy comparison and a vertical card
layout on mobile for better readability.

| SoloMost popularFor indie hackers.$249billed annually/monthBuy now| TeamFor
growing teams.$499billed annually/monthBuy now| EnterpriseFor large
organizations.CustomContact sales  
---|---|---|---  
Features| | |   
Number of developers| 1| 5| Unlimited  
Projects| | |   
GitHub repository access| | |   
Updates| Patch & minor| All updates| All updates  
Support| Community| Priority| 24/7  
Security| | |   
SSO| | |   
Audit logs| | |   
Custom security review| | |   
  
  * Solo

Most popular

For indie hackers.

$249

billed annually/month

Buy now

Features

Number of developers

1

Projects

GitHub repository access

Updates

Patch & minor

Support

Community

Security

SSO

Audit logs

Custom security review

  * Team

For growing teams.

$499

billed annually/month

Buy now

Features

Number of developers

5

Projects

GitHub repository access

Updates

All updates

Support

Priority

Security

SSO

Audit logs

Custom security review

  * Enterprise

For large organizations.

Custom

Contact sales

Features

Number of developers

Unlimited

Projects

GitHub repository access

Updates

All updates

Support

24/7

Security

SSO

Audit logs

Custom security review

### Tiers

Use the `tiers` prop as an array of objects to define your pricing plans. Each
tier object supports the following properties:

  * `id: string` \- Unique identifier for the tier (required)
  * `title?: string` \- Name of the pricing plan
  * `description?: string` \- Short description of the plan
  * `price?: string` \- The current price of the plan (e.g., "$99", "€99", "Free")
  * `discount?: string` \- The discounted price that will display the `price` with strikethrough (e.g., "$79", "€79")
  * `billingCycle?: string` \- The unit price period that appears next to the price (e.g., "/month", "/seat/month")
  * `billingPeriod?: string` \- Additional billing context that appears above the billing cycle (e.g., "billed monthly")
  * `badge?: string | BadgeProps` \- Display a badge next to the title `{ color: 'primary', variant: 'subtle' }`
  * `button?: ButtonProps` \- Configure the CTA button `{ size: 'lg', block: true }`
  * `highlight?: boolean` \- Whether to visually emphasize this tier as the recommended option

| SoloMost popularFor indie hackers.$249billed annually/monthBuy now| TeamFor
growing teams.$499billed annually/monthBuy now| EnterpriseFor large
organizations.CustomContact sales  
---|---|---|---  
  
  * Solo

Most popular

For indie hackers.

$249

billed annually/month

Buy now

  * Team

For growing teams.

$499

billed annually/month

Buy now

  * Enterprise

For large organizations.

Custom

Contact sales

    
    
    <script setup lang="ts">
    const tiers = ref([
      {
        id: 'solo',
        title: 'Solo',
        description: 'For indie hackers.',
        price: '$249',
        billingCycle: '/month',
        billingPeriod: 'billed annually',
        badge: 'Most popular',
        button: {
          label: 'Buy now',
          variant: 'subtle'
        }
      },
      {
        id: 'team',
        title: 'Team',
        description: 'For growing teams.',
        price: '$499',
        billingCycle: '/month',
        billingPeriod: 'billed annually',
        button: {
          label: 'Buy now'
        },
        highlight: true
      },
      {
        id: 'enterprise',
        title: 'Enterprise',
        description: 'For large organizations.',
        price: 'Custom',
        button: {
          label: 'Contact sales',
          color: 'neutral'
        }
      }
    ])
    </script>
    
    <template>
      <UPricingTable :tiers="tiers" />
    </template>
    

Expand code

### Sections

Use the `sections` prop to organize features into logical groups. Each section
represents a category of features that you want to compare across different
pricing tiers.

  * `title: string` \- The heading for the feature section
  * `features: PricingTableSectionFeature[]` \- An array of features with their availability in each tier: 
    * Each feature requires a `title` and a `tiers` object mapping tier IDs to values
    * Boolean values (`true`/`false`) will display as checkmarks (✓) or minus icons (-)
    * String values will be shown as text (e.g., "Unlimited", "Up to 5 users")
    * Numeric values will be displayed as is (e.g., 10, 100)

| SoloFor indie hackers.$249 /monthBuy now| TeamFor growing teams.$499
/monthBuy now| EnterpriseFor large organizations.CustomContact sales  
---|---|---|---  
Features| | |   
Number of developers| 1| 5| Unlimited  
Projects| | |   
Security| | |   
SSO| | |   
  
  * Solo

For indie hackers.

$249

/month

Buy now

Features

Number of developers

1

Projects

Security

SSO

  * Team

For growing teams.

$499

/month

Buy now

Features

Number of developers

5

Projects

Security

SSO

  * Enterprise

For large organizations.

Custom

Contact sales

Features

Number of developers

Unlimited

Projects

Security

SSO

    
    
    <script setup lang="ts">
    const tiers = ref([
      {
        id: 'solo',
        title: 'Solo',
        price: '$249',
        description: 'For indie hackers.',
        billingCycle: '/month',
        button: {
          label: 'Buy now',
          variant: 'subtle'
        }
      },
      {
        id: 'team',
        title: 'Team',
        price: '$499',
        description: 'For growing teams.',
        billingCycle: '/month',
        button: {
          label: 'Buy now'
        }
      },
      {
        id: 'enterprise',
        title: 'Enterprise',
        price: 'Custom',
        description: 'For large organizations.',
        button: {
          label: 'Contact sales',
          color: 'neutral'
        }
      }
    ])
    const sections = ref([
      {
        title: 'Features',
        features: [
          {
            title: 'Number of developers',
            tiers: {
              solo: '1',
              team: '5',
              enterprise: 'Unlimited'
            }
          },
          {
            title: 'Projects',
            tiers: {
              solo: true,
              team: true,
              enterprise: true
            }
          }
        ]
      },
      {
        title: 'Security',
        features: [
          {
            title: 'SSO',
            tiers: {
              solo: false,
              team: true,
              enterprise: true
            }
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UPricingTable :tiers="tiers" :sections="sections" />
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`tiers`| | `PricingTableTier[]`The pricing tiers to display in the table. Each tier represents a pricing plan with its own title, description, price, and features.Show properties

  * `title?: string`
  * `description?: string`
  * `highlight?: boolean`Display a ring around the pricing plan to highlight it.
  * `badge?: string | BadgeProps`Display a badge next to the title. Can be a string or an object. `{ color: 'primary', variant: 'subtle' }`
  * `button?: ButtonProps`Display a buy button at the bottom. `{ size: 'lg', block: true }` Use the `onClick` field to add a click handler.
  * `billingCycle?: string`The unit price period that appears next to the price. Typically used to show the recurring interval.
  * `billingPeriod?: string`Additional billing context that appears above the billing cycle. Typically used to show the actual billing frequency.
  * `price?: string`The current price of the plan. When used with `discount`, this becomes the original price.
  * `discount?: string`The discounted price of the plan. When provided, the `price` prop will be displayed as strikethrough.
  * `id: string`

  
`sections`| | `PricingTableSection<PricingTableTier>[]`The sections of features to display in the table. Each section contains a title and a list of features with their availability in each tier.  
`caption`| | ` string`The caption to display above the table.  
`ui`| | ` { root?: ClassNameValue; table?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; caption?: ClassNameValue; ... 22 more ...; featureValue?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`caption`| `{}`  
`tier`| `{ tier: PricingTableTier; }`  
`tier-title`| `{ tier: PricingTableTier; }`  
`tier-description`| `{ tier: PricingTableTier; }`  
`tier-badge`| `{ tier: PricingTableTier; }`  
`tier-button`| `{ tier: PricingTableTier; }`  
`tier-billing`| `{ tier: PricingTableTier; }`  
`tier-discount`| `{ tier: PricingTableTier; }`  
`tier-price`| `{ tier: PricingTableTier; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pricingTable: {
          slots: {
            root: 'w-full relative',
            table: 'w-full table-fixed border-separate border-spacing-x-0 hidden md:table',
            list: 'md:hidden flex flex-col gap-6 w-full',
            item: 'p-6 flex flex-col border border-default rounded-lg',
            caption: 'sr-only',
            thead: '',
            tbody: '',
            tr: '',
            th: 'py-4 font-normal text-left border-b border-default',
            td: 'px-6 py-4 text-center border-b border-default',
            tier: 'p-6 text-left font-normal',
            tierTitleWrapper: 'flex items-center gap-3',
            tierTitle: 'text-lg font-semibold text-highlighted',
            tierDescription: 'text-sm font-normal text-muted mt-1',
            tierBadge: 'truncate',
            tierPriceWrapper: 'flex items-center gap-1 mt-4',
            tierPrice: 'text-highlighted text-3xl sm:text-4xl font-semibold',
            tierDiscount: 'text-muted line-through text-xl sm:text-2xl',
            tierBilling: 'flex flex-col justify-between min-w-0',
            tierBillingPeriod: 'text-toned truncate text-xs font-medium',
            tierBillingCycle: 'text-muted truncate text-xs font-medium',
            tierButton: 'mt-6',
            tierFeatureIcon: 'size-5 shrink-0',
            section: 'mt-6 flex flex-col gap-2',
            sectionTitle: 'font-semibold text-sm text-highlighted',
            feature: 'flex items-center justify-between gap-1',
            featureTitle: 'text-sm text-default',
            featureValue: 'text-sm text-muted flex justify-center min-w-5'
          },
          variants: {
            section: {
              true: {
                tr: '*:pt-8'
              }
            },
            active: {
              true: {
                tierFeatureIcon: 'text-primary'
              }
            },
            highlight: {
              true: {
                tier: 'bg-elevated/50 border-x border-t border-default rounded-t-lg',
                td: 'bg-elevated/50 border-x border-default',
                item: 'bg-elevated/50'
              }
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            pricingTable: {
              slots: {
                root: 'w-full relative',
                table: 'w-full table-fixed border-separate border-spacing-x-0 hidden md:table',
                list: 'md:hidden flex flex-col gap-6 w-full',
                item: 'p-6 flex flex-col border border-default rounded-lg',
                caption: 'sr-only',
                thead: '',
                tbody: '',
                tr: '',
                th: 'py-4 font-normal text-left border-b border-default',
                td: 'px-6 py-4 text-center border-b border-default',
                tier: 'p-6 text-left font-normal',
                tierTitleWrapper: 'flex items-center gap-3',
                tierTitle: 'text-lg font-semibold text-highlighted',
                tierDescription: 'text-sm font-normal text-muted mt-1',
                tierBadge: 'truncate',
                tierPriceWrapper: 'flex items-center gap-1 mt-4',
                tierPrice: 'text-highlighted text-3xl sm:text-4xl font-semibold',
                tierDiscount: 'text-muted line-through text-xl sm:text-2xl',
                tierBilling: 'flex flex-col justify-between min-w-0',
                tierBillingPeriod: 'text-toned truncate text-xs font-medium',
                tierBillingCycle: 'text-muted truncate text-xs font-medium',
                tierButton: 'mt-6',
                tierFeatureIcon: 'size-5 shrink-0',
                section: 'mt-6 flex flex-col gap-2',
                sectionTitle: 'font-semibold text-sm text-highlighted',
                feature: 'flex items-center justify-between gap-1',
                featureTitle: 'text-sm text-default',
                featureValue: 'text-sm text-muted flex justify-center min-w-5'
              },
              variants: {
                section: {
                  true: {
                    tr: '*:pt-8'
                  }
                },
                active: {
                  true: {
                    tierFeatureIcon: 'text-primary'
                  }
                },
                highlight: {
                  true: {
                    tier: 'bg-elevated/50 border-x border-t border-default rounded-t-lg',
                    td: 'bg-elevated/50 border-x border-default',
                    item: 'bg-elevated/50'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            pricingTable: {
              slots: {
                root: 'w-full relative',
                table: 'w-full table-fixed border-separate border-spacing-x-0 hidden md:table',
                list: 'md:hidden flex flex-col gap-6 w-full',
                item: 'p-6 flex flex-col border border-default rounded-lg',
                caption: 'sr-only',
                thead: '',
                tbody: '',
                tr: '',
                th: 'py-4 font-normal text-left border-b border-default',
                td: 'px-6 py-4 text-center border-b border-default',
                tier: 'p-6 text-left font-normal',
                tierTitleWrapper: 'flex items-center gap-3',
                tierTitle: 'text-lg font-semibold text-highlighted',
                tierDescription: 'text-sm font-normal text-muted mt-1',
                tierBadge: 'truncate',
                tierPriceWrapper: 'flex items-center gap-1 mt-4',
                tierPrice: 'text-highlighted text-3xl sm:text-4xl font-semibold',
                tierDiscount: 'text-muted line-through text-xl sm:text-2xl',
                tierBilling: 'flex flex-col justify-between min-w-0',
                tierBillingPeriod: 'text-toned truncate text-xs font-medium',
                tierBillingCycle: 'text-muted truncate text-xs font-medium',
                tierButton: 'mt-6',
                tierFeatureIcon: 'size-5 shrink-0',
                section: 'mt-6 flex flex-col gap-2',
                sectionTitle: 'font-semibold text-sm text-highlighted',
                feature: 'flex items-center justify-between gap-1',
                featureTitle: 'text-sm text-default',
                featureValue: 'text-sm text-muted flex justify-center min-w-5'
              },
              variants: {
                section: {
                  true: {
                    tr: '*:pt-8'
                  }
                },
                active: {
                  true: {
                    tierFeatureIcon: 'text-primary'
                  }
                },
                highlight: {
                  true: {
                    tier: 'bg-elevated/50 border-x border-t border-default rounded-t-lg',
                    td: 'bg-elevated/50 border-x border-default',
                    item: 'bg-elevated/50'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[PricingPlansDisplay a list of pricing plans in a responsive grid
layout.](/components/pricing-plans)[ProgressAn indicator showing the progress
of a task.](/components/progress)

