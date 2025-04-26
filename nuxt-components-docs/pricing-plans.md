<!-- source: https://ui.nuxt.com/components/pricing-plans --> # PricingPlansPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PricingPlans.vue)

Display a list of pricing plans in a responsive grid layout.

## Usage

The PricingPlans component provides a flexible layout to display a list of
[PricingPlan](/components/pricing-plan) components using either the default
slot or the `plans` prop.

    
    
    <template>
      <UPricingPlans>
        <UPricingPlan
          v-for="(plan, index) in plans"
          :key="index"
          v-bind="plan"
        />
      </UPricingPlans>
    </template>
    

The grid columns will be automatically calculated based on the number of
plans, this works with the `plans` prop but also with the default slot.

### Plans

Use the `plans` prop as an array of objects with the properties of the
[PricingPlan](/components/pricing-plan#props) component.

Solo

Tailored for indie hackers.

$249

  * One developer
  * Lifetime access

Buy now

Startup

Best suited for small teams.

$499

  * Up to 5 developers
  * Everything in Solo

Buy now

Organization

Ideal for larger teams and organizations.

$999

  * Up to 20 developers
  * Everything in Startup

Buy now

    
    
    <script setup lang="ts">
    const plans = ref([
      {
        title: 'Solo',
        description: 'Tailored for indie hackers.',
        price: '$249',
        features: [
          'One developer',
          'Lifetime access'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Startup',
        description: 'Best suited for small teams.',
        price: '$499',
        features: [
          'Up to 5 developers',
          'Everything in Solo'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Organization',
        description: 'Ideal for larger teams and organizations.',
        price: '$999',
        features: [
          'Up to 20 developers',
          'Everything in Startup'
        ],
        button: {
          label: 'Buy now'
        }
      }
    ])
    </script>
    
    <template>
      <UPricingPlans :plans="plans" />
    </template>
    

Expand code

### Orientation

Use the `orientation` prop to change the orientation of the PricingPlans.
Defaults to `horizontal`.

orientation

vertical

Solo

Tailored for indie hackers.

  * One developer
  * Lifetime access

$249

Buy now

Startup

Best suited for small teams.

  * Up to 5 developers
  * Everything in Solo

$499

Buy now

Organization

Ideal for larger teams and organizations.

  * Up to 20 developers
  * Everything in Startup

$999

Buy now

    
    
    <script setup lang="ts">
    const plans = ref([
      {
        title: 'Solo',
        description: 'Tailored for indie hackers.',
        price: '$249',
        features: [
          'One developer',
          'Lifetime access'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Startup',
        description: 'Best suited for small teams.',
        price: '$499',
        features: [
          'Up to 5 developers',
          'Everything in Solo'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Organization',
        description: 'Ideal for larger teams and organizations.',
        price: '$999',
        features: [
          'Up to 20 developers',
          'Everything in Startup'
        ],
        button: {
          label: 'Buy now'
        }
      }
    ])
    </script>
    
    <template>
      <UPricingPlans orientation="vertical" :plans="plans" />
    </template>
    

Expand code

When using the `plans` prop instead of the default slot, the `orientation` of
the plans is automatically reversed, `horizontal` to `vertical` and vice
versa.

### Compact

Use the `compact` prop to reduce the padding between the plans when one of the
plans is scaled for a better visual balance.

Solo

Tailored for indie hackers.

$249

  * One developer
  * Lifetime access

Buy now

Startup

Best suited for small teams.

$499

  * Up to 5 developers
  * Everything in Solo

Buy now

Organization

Ideal for larger teams and organizations.

$999

  * Up to 20 developers
  * Everything in Startup

Buy now

    
    
    <script setup lang="ts">
    const plans = ref([
      {
        title: 'Solo',
        description: 'Tailored for indie hackers.',
        price: '$249',
        features: [
          'One developer',
          'Lifetime access'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Startup',
        description: 'Best suited for small teams.',
        price: '$499',
        scale: true,
        features: [
          'Up to 5 developers',
          'Everything in Solo'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Organization',
        description: 'Ideal for larger teams and organizations.',
        price: '$999',
        features: [
          'Up to 20 developers',
          'Everything in Startup'
        ],
        button: {
          label: 'Buy now'
        }
      }
    ])
    </script>
    
    <template>
      <UPricingPlans compact :plans="plans" />
    </template>
    

Expand code

### Scale

Use the `scale` prop to adjust the spacing between the plans when one of the
plans is scaled for a better visual balance.

Solo

Tailored for indie hackers.

$249

  * One developer
  * Lifetime access

Buy now

Startup

Best suited for small teams.

$499

  * Up to 5 developers
  * Everything in Solo

Buy now

Organization

Ideal for larger teams and organizations.

$999

  * Up to 20 developers
  * Everything in Startup

Buy now

    
    
    <script setup lang="ts">
    const plans = ref([
      {
        title: 'Solo',
        description: 'Tailored for indie hackers.',
        price: '$249',
        features: [
          'One developer',
          'Lifetime access'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Startup',
        description: 'Best suited for small teams.',
        price: '$499',
        scale: true,
        features: [
          'Up to 5 developers',
          'Everything in Solo'
        ],
        button: {
          label: 'Buy now'
        }
      },
      {
        title: 'Organization',
        description: 'Ideal for larger teams and organizations.',
        price: '$999',
        features: [
          'Up to 20 developers',
          'Everything in Startup'
        ],
        button: {
          label: 'Buy now'
        }
      }
    ])
    </script>
    
    <template>
      <UPricingPlans scale :plans="plans" />
    </template>
    

Expand code

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a page

Use the PricingPlans component in a page to create a pricing page:

pages/pricing/index.vue

    
    
    <script setup lang="ts">
    const { data: plans } = await useAsyncData('plans', () => queryCollection('plans').all())
    </script>
    
    <template>
      <UPage>
        <UPageHero title="Pricing" />
    
        <UPageBody>
          <UContainer>
            <UPricingPlans :plans="plans" />
          </UContainer>
        </UPageBody>
      </UPage>
    </template>
    

In this example, the `plans` are fetched using `queryCollection` from the
`@nuxt/content` module.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`  
`compact`| `false`| `boolean`  
`scale`| `false`| `boolean`  
`plans`| | ` PricingPlanProps[]`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `title?: string`
  * `description?: string`
  * `badge?: string | BadgeProps`Display a badge next to the title. Can be a string or an object. `{ color: 'primary', variant: 'subtle' }`
  * `billingCycle?: string`The unit price period that appears next to the price. Typically used to show the recurring interval.
  * `billingPeriod?: string`Additional billing context that appears above the billing cycle. Typically used to show the actual billing frequency.
  * `price?: string`The current price of the plan. When used with `discount`, this becomes the original price.
  * `discount?: string`The discounted price of the plan. When provided, the `price` prop will be displayed as strikethrough.
  * `features?: string[] | PricingPlanFeature[]`Display a list of features under the price. Can be an array of strings or an array of objects.
  * `button?: ButtonProps`Display a buy button at the bottom. `{ size: 'lg', block: true }` Use the `onClick` field to add a click handler.
  * `tagline?: string`Display a tagline highlighting the pricing value proposition.
  * `terms?: string`Display terms at the bottom.
  * `orientation?: "horizontal" | "vertical"`The orientation of the pricing plan. Defaults to `'vertical'`.
  * `variant?: "solid" | "outline" | "soft" | "subtle"`Defaults to `'outline'`.
  * `highlight?: boolean`Display a ring around the pricing plan to highlight it.
  * `scale?: boolean`Enlarge the plan to make it more prominent.
  * `class?: any`
  * `ui?: { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; titleWrapper?: ClassNameValue; ... 15 more ...; terms?: ClassNameValue; }`

  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pricingPlans: {
          base: 'flex flex-col gap-y-8',
          variants: {
            orientation: {
              horizontal: 'lg:grid lg:grid-cols-[repeat(var(--count),minmax(0,1fr))]',
              vertical: ''
            },
            compact: {
              false: 'gap-x-8'
            },
            scale: {
              true: ''
            }
          },
          compoundVariants: [
            {
              compact: false,
              scale: true,
              class: 'lg:gap-x-13'
            }
          ]
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
            pricingPlans: {
              base: 'flex flex-col gap-y-8',
              variants: {
                orientation: {
                  horizontal: 'lg:grid lg:grid-cols-[repeat(var(--count),minmax(0,1fr))]',
                  vertical: ''
                },
                compact: {
                  false: 'gap-x-8'
                },
                scale: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  compact: false,
                  scale: true,
                  class: 'lg:gap-x-13'
                }
              ]
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
            pricingPlans: {
              base: 'flex flex-col gap-y-8',
              variants: {
                orientation: {
                  horizontal: 'lg:grid lg:grid-cols-[repeat(var(--count),minmax(0,1fr))]',
                  vertical: ''
                },
                compact: {
                  false: 'gap-x-8'
                },
                scale: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  compact: false,
                  scale: true,
                  class: 'lg:gap-x-13'
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

[PricingPlanA customizable pricing plan to display in a pricing
page.](/components/pricing-plan)[PricingTableA responsive pricing table
component that displays tiered pricing plans with feature
comparisons.](/components/pricing-table)

