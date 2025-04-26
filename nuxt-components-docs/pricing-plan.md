<!-- source: https://ui.nuxt.com/components/pricing-plan --> # PricingPlanPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PricingPlan.vue)

A customizable pricing plan to display in a pricing page.

## Usage

The PricingPlan component provides a flexible way to display a pricing plan
with customizable content including title, description, price, features, etc.

Solo

Most popular

For bootstrappers and indie hackers.

$249

$199

/month

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Unlimited patch & minor updates
  * Lifetime access

Buy now

[](/components/pricing-plans)Use the [`PricingPlans`](/components/pricing-
plans) component to display multiple pricing plans in a responsive grid
layout.

### Title

Use the `title` prop to set the title of the PricingPlan.

title

Solo

    
    
    <template>
      <UPricingPlan title="Solo" class="w-96" />
    </template>
    

### Description

Use the `description` prop to set the description of the PricingPlan.

description

Solo

For bootstrappers and indie hackers.

    
    
    <template>
      <UPricingPlan title="Solo" description="For bootstrappers and indie hackers." />
    </template>
    

### Badge

Use the `badge` prop to display a [Badge](/components/badge) next to the title
of the PricingPlan.

badge

Solo

Most popular

For bootstrappers and indie hackers.

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        badge="Most popular"
      />
    </template>
    

You can pass any property from the [Badge](/components/badge#props) component
to customize it.

Solo

Most popular

For bootstrappers and indie hackers.

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        :badge="{
          label: 'Most popular',
          color: 'neutral',
          variant: 'solid'
        }"
      />
    </template>
    

### Price

Use the `price` prop to set the price of the PricingPlan.

price

Solo

For bootstrappers and indie hackers.

$249

    
    
    <template>
      <UPricingPlan title="Solo" description="For bootstrappers and indie hackers." price="$249" />
    </template>
    

### Discount

Use the `discount` prop to set a discounted price that will be displayed
alongside the original price (which will be shown with a strikethrough).

price

discount

Solo

For bootstrappers and indie hackers.

$249

$199

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        discount="$199"
      />
    </template>
    

### Billing

Use the `billing-cycle` and/or `billing-period` props to display the billing
information of the PricingPlan.

price

billingCycle

billingPeriod

Solo

For bootstrappers and indie hackers.

$9

billed annually/month

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$9"
        billing-cycle="/month"
        billing-period="billed annually"
      />
    </template>
    

### Features

Use the `features` prop as an array of string to display a list of features on
the PricingPlan:

Solo

For bootstrappers and indie hackers.

$249

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Unlimited patch & minor updates
  * Lifetime access

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Unlimited patch & minor updates',
          'Lifetime access'
        ]"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.success` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.success` key.

You can also pass an array of objects with the following properties:

  * `title: string`
  * `icon?: string`

Solo

For bootstrappers and indie hackers.

$249

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Unlimited patch & minor updates
  * Lifetime access

    
    
    <script setup lang="ts">
    const features = ref([
      {
        title: 'One developer',
        icon: 'i-lucide-user'
      },
      {
        title: 'Unlimited projects',
        icon: 'i-lucide-infinity'
      },
      {
        title: 'Access to GitHub repository',
        icon: 'i-lucide-github'
      },
      {
        title: 'Unlimited patch & minor updates',
        icon: 'i-lucide-refresh-cw'
      },
      {
        title: 'Lifetime access',
        icon: 'i-lucide-clock'
      }
    ])
    </script>
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="features"
      />
    </template>
    

### Button

Use the `button` prop with any property from the [Button](/components/button)
component to display a button at the bottom of the PricingPlan.

button.label

Solo

For bootstrappers and indie hackers.

$249

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Unlimited patch & minor updates
  * Lifetime access

Buy now

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Unlimited patch & minor updates',
          'Lifetime access'
        ]"
        :button="{
          label: 'Buy now'
        }"
      />
    </template>
    

Use the `onClick` field to add a click handler to trigger the plan purchase.

### Variant

Use the `variant` prop to change the variant of the PricingPlan.

variant

subtle

Solo

For bootstrappers and indie hackers.

$249

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Unlimited patch & minor updates
  * Lifetime access

Buy now

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Unlimited patch & minor updates',
          'Lifetime access'
        ]"
        :button="{
          label: 'Buy now'
        }"
        variant="subtle"
      />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the PricingPlan.
Defaults to `vertical`.

orientation

horizontal

variant

outline

Solo

For bootstrappers and indie hackers.

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Lifetime access

$249

Buy now

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Lifetime access'
        ]"
        :button="{
          label: 'Buy now'
        }"
        orientation="horizontal"
        variant="outline"
      />
    </template>
    

### Tagline

Use the `tagline` prop to display a tagline text above the price.

tagline

Solo

For bootstrappers and indie hackers.

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Lifetime access

Pay once, own it forever

$249

Buy now

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Lifetime access'
        ]"
        :button="{
          label: 'Buy now'
        }"
        orientation="horizontal"
        tagline="Pay once, own it forever"
      />
    </template>
    

### Terms

Use the `terms` prop to display terms below the price.

terms

Solo

For bootstrappers and indie hackers.

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Lifetime access

Pay once, own it forever

$249

Buy now

Invoices and receipts available.

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Lifetime access'
        ]"
        :button="{
          label: 'Buy now'
        }"
        orientation="horizontal"
        tagline="Pay once, own it forever"
        terms="Invoices and receipts available."
      />
    </template>
    

### Highlight

Use the `highlight` prop to display a highlighted border around the
PricingPlan.

highlight

true

Solo

For bootstrappers and indie hackers.

$249

  * One developer
  * Unlimited projects
  * Access to GitHub repository
  * Unlimited patch & minor updates
  * Lifetime access

Buy now

    
    
    <template>
      <UPricingPlan
        title="Solo"
        description="For bootstrappers and indie hackers."
        price="$249"
        :features="[
          'One developer',
          'Unlimited projects',
          'Access to GitHub repository',
          'Unlimited patch & minor updates',
          'Lifetime access'
        ]"
        :button="{
          label: 'Buy now'
        }"
        highlight
      />
    </template>
    

### Scale

Use the `scale` prop to make a PricingPlan bigger than the others.

[](/components/pricing-plans#scale)Check out the PricingPlans's `scale`
example to see how it works as it's hard to demonstrate by itself.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`  
`title`| | ` string`  
`description`| | ` string`  
`variant`| `'outline'`| ` "solid" | "outline" | "soft" | "subtle"`  
`highlight`| | `boolean`Display a ring around the pricing plan to highlight it.  
`badge`| | ` string | BadgeProps`Display a badge next to the title. Can be a string or an object. `{ color: 'primary', variant: 'subtle' }`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `label?: string | number`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `variant?: "solid" | "outline" | "soft" | "subtle"`Defaults to `'solid'`.
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `trailingIcon?: string`Display an icon on the right side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.

  
`button`| | ` ButtonProps`Display a buy button at the bottom. `{ size: 'lg', block: true }` Use the `onClick` field to add a click handler.Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`features`| | ` string[] | PricingPlanFeature[]`Display a list of features under the price. Can be an array of strings or an array of objects.Show properties

  * `title: string`
  * `icon?: string`Defaults to `appConfig.ui.icons.success`.

  
`billingCycle`| | ` string`The unit price period that appears next to the price. Typically used to show the recurring interval.  
`billingPeriod`| | ` string`Additional billing context that appears above the billing cycle. Typically used to show the actual billing frequency.  
`price`| | ` string`The current price of the plan. When used with `discount`, this becomes the original price.  
`discount`| | ` string`The discounted price of the plan. When provided, the `price` prop will be displayed as strikethrough.  
`tagline`| | ` string`Display a tagline highlighting the pricing value proposition.  
`terms`| | ` string`Display terms at the bottom.  
`scale`| | `boolean`Enlarge the plan to make it more prominent.  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; titleWrapper?: ClassNameValue; ... 15 more ...; terms?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`badge`| `{}`  
`title`| `{}`  
`description`| `{}`  
`price`| `{}`  
`discount`| `{}`  
`billing`| `{}`  
`features`| `{}`  
`button`| `{}`  
`header`| `{}`  
`body`| `{}`  
`footer`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pricingPlan: {
          slots: {
            root: 'relative grid rounded-lg p-6 lg:p-8 xl:p-10 gap-6',
            header: '',
            body: 'flex flex-col min-w-0',
            footer: 'flex flex-col gap-6 items-center',
            titleWrapper: 'flex items-center gap-3',
            title: 'text-highlighted text-2xl sm:text-3xl text-pretty font-semibold',
            description: 'text-muted text-base text-pretty mt-2',
            priceWrapper: 'flex items-center gap-1',
            price: 'text-highlighted text-3xl sm:text-4xl font-semibold',
            discount: 'text-muted line-through text-xl sm:text-2xl',
            billing: 'flex flex-col justify-between min-w-0',
            billingPeriod: 'text-toned truncate text-xs font-medium',
            billingCycle: 'text-muted truncate text-xs font-medium',
            features: 'flex flex-col gap-3 flex-1 mt-6 grow-0',
            feature: 'flex items-center gap-2 min-w-0',
            featureIcon: 'size-5 shrink-0 text-primary',
            featureTitle: 'text-muted text-sm truncate',
            badge: '',
            button: '',
            tagline: 'text-base font-semibold text-default',
            terms: 'text-xs/5 text-muted text-center text-balance'
          },
          variants: {
            orientation: {
              horizontal: {
                root: 'grid-cols-1 lg:grid-cols-3 justify-between divide-y lg:divide-y-0 lg:divide-x divide-default',
                body: 'lg:col-span-2 pb-6 lg:pb-0 lg:pr-6 justify-center',
                footer: 'lg:justify-center lg:items-center lg:p-6 lg:max-w-xs lg:w-full lg:mx-auto',
                features: 'lg:grid lg:grid-cols-2 lg:mt-12'
              },
              vertical: {
                footer: 'justify-end',
                priceWrapper: 'mt-6'
              }
            },
            variant: {
              solid: {
                root: 'bg-inverted',
                title: 'text-inverted',
                description: 'text-dimmed',
                price: 'text-inverted',
                discount: 'text-dimmed',
                billingCycle: 'text-dimmed',
                billingPeriod: 'text-dimmed',
                featureTitle: 'text-dimmed'
              },
              outline: {
                root: 'bg-default ring ring-default'
              },
              soft: {
                root: 'bg-elevated/50'
              },
              subtle: {
                root: 'bg-elevated/50 ring ring-default'
              }
            },
            highlight: {
              true: {
                root: 'ring-2 ring-inset ring-primary'
              }
            },
            scale: {
              true: {
                root: 'lg:scale-[1.1] lg:z-[1]'
              }
            }
          },
          compoundVariants: [
            {
              orientation: 'horizontal',
              variant: 'soft',
              class: {
                root: 'divide-accented'
              }
            },
            {
              orientation: 'horizontal',
              variant: 'subtle',
              class: {
                root: 'divide-accented'
              }
            }
          ],
          defaultVariants: {
            variant: 'outline'
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
            pricingPlan: {
              slots: {
                root: 'relative grid rounded-lg p-6 lg:p-8 xl:p-10 gap-6',
                header: '',
                body: 'flex flex-col min-w-0',
                footer: 'flex flex-col gap-6 items-center',
                titleWrapper: 'flex items-center gap-3',
                title: 'text-highlighted text-2xl sm:text-3xl text-pretty font-semibold',
                description: 'text-muted text-base text-pretty mt-2',
                priceWrapper: 'flex items-center gap-1',
                price: 'text-highlighted text-3xl sm:text-4xl font-semibold',
                discount: 'text-muted line-through text-xl sm:text-2xl',
                billing: 'flex flex-col justify-between min-w-0',
                billingPeriod: 'text-toned truncate text-xs font-medium',
                billingCycle: 'text-muted truncate text-xs font-medium',
                features: 'flex flex-col gap-3 flex-1 mt-6 grow-0',
                feature: 'flex items-center gap-2 min-w-0',
                featureIcon: 'size-5 shrink-0 text-primary',
                featureTitle: 'text-muted text-sm truncate',
                badge: '',
                button: '',
                tagline: 'text-base font-semibold text-default',
                terms: 'text-xs/5 text-muted text-center text-balance'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'grid-cols-1 lg:grid-cols-3 justify-between divide-y lg:divide-y-0 lg:divide-x divide-default',
                    body: 'lg:col-span-2 pb-6 lg:pb-0 lg:pr-6 justify-center',
                    footer: 'lg:justify-center lg:items-center lg:p-6 lg:max-w-xs lg:w-full lg:mx-auto',
                    features: 'lg:grid lg:grid-cols-2 lg:mt-12'
                  },
                  vertical: {
                    footer: 'justify-end',
                    priceWrapper: 'mt-6'
                  }
                },
                variant: {
                  solid: {
                    root: 'bg-inverted',
                    title: 'text-inverted',
                    description: 'text-dimmed',
                    price: 'text-inverted',
                    discount: 'text-dimmed',
                    billingCycle: 'text-dimmed',
                    billingPeriod: 'text-dimmed',
                    featureTitle: 'text-dimmed'
                  },
                  outline: {
                    root: 'bg-default ring ring-default'
                  },
                  soft: {
                    root: 'bg-elevated/50'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default'
                  }
                },
                highlight: {
                  true: {
                    root: 'ring-2 ring-inset ring-primary'
                  }
                },
                scale: {
                  true: {
                    root: 'lg:scale-[1.1] lg:z-[1]'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  variant: 'soft',
                  class: {
                    root: 'divide-accented'
                  }
                },
                {
                  orientation: 'horizontal',
                  variant: 'subtle',
                  class: {
                    root: 'divide-accented'
                  }
                }
              ],
              defaultVariants: {
                variant: 'outline'
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
            pricingPlan: {
              slots: {
                root: 'relative grid rounded-lg p-6 lg:p-8 xl:p-10 gap-6',
                header: '',
                body: 'flex flex-col min-w-0',
                footer: 'flex flex-col gap-6 items-center',
                titleWrapper: 'flex items-center gap-3',
                title: 'text-highlighted text-2xl sm:text-3xl text-pretty font-semibold',
                description: 'text-muted text-base text-pretty mt-2',
                priceWrapper: 'flex items-center gap-1',
                price: 'text-highlighted text-3xl sm:text-4xl font-semibold',
                discount: 'text-muted line-through text-xl sm:text-2xl',
                billing: 'flex flex-col justify-between min-w-0',
                billingPeriod: 'text-toned truncate text-xs font-medium',
                billingCycle: 'text-muted truncate text-xs font-medium',
                features: 'flex flex-col gap-3 flex-1 mt-6 grow-0',
                feature: 'flex items-center gap-2 min-w-0',
                featureIcon: 'size-5 shrink-0 text-primary',
                featureTitle: 'text-muted text-sm truncate',
                badge: '',
                button: '',
                tagline: 'text-base font-semibold text-default',
                terms: 'text-xs/5 text-muted text-center text-balance'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'grid-cols-1 lg:grid-cols-3 justify-between divide-y lg:divide-y-0 lg:divide-x divide-default',
                    body: 'lg:col-span-2 pb-6 lg:pb-0 lg:pr-6 justify-center',
                    footer: 'lg:justify-center lg:items-center lg:p-6 lg:max-w-xs lg:w-full lg:mx-auto',
                    features: 'lg:grid lg:grid-cols-2 lg:mt-12'
                  },
                  vertical: {
                    footer: 'justify-end',
                    priceWrapper: 'mt-6'
                  }
                },
                variant: {
                  solid: {
                    root: 'bg-inverted',
                    title: 'text-inverted',
                    description: 'text-dimmed',
                    price: 'text-inverted',
                    discount: 'text-dimmed',
                    billingCycle: 'text-dimmed',
                    billingPeriod: 'text-dimmed',
                    featureTitle: 'text-dimmed'
                  },
                  outline: {
                    root: 'bg-default ring ring-default'
                  },
                  soft: {
                    root: 'bg-elevated/50'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default'
                  }
                },
                highlight: {
                  true: {
                    root: 'ring-2 ring-inset ring-primary'
                  }
                },
                scale: {
                  true: {
                    root: 'lg:scale-[1.1] lg:z-[1]'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  variant: 'soft',
                  class: {
                    root: 'divide-accented'
                  }
                },
                {
                  orientation: 'horizontal',
                  variant: 'subtle',
                  class: {
                    root: 'divide-accented'
                  }
                }
              ],
              defaultVariants: {
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[PopoverA non-modal dialog that floats around a trigger
element.](/components/popover)[PricingPlansDisplay a list of pricing plans in
a responsive grid layout.](/components/pricing-plans)

