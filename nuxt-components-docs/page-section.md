<!-- source: https://ui.nuxt.com/components/page-section --> # PageSectionPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageSection.vue)

A responsive section for your pages.

## Usage

The PageSection component wraps your content in a
[Container](/components/container) while maintaining full-width flexibility
making it easy to add background colors, images or patterns. It provides a
flexible way to display content with an illustration in the default slot.

Features

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

  * [](/getting-started/icons)

Icons

Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.

  * [](/getting-started/fonts)

Fonts

Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.

  * [](/getting-started/color-mode)

Color Mode

Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.

Use it after a [PageHero](/components/page-hero) component:

    
    
    <template>
      <UPageHero />
    
      <UPageSection />
    </template>
    

### Title

Use the `title` prop to set the title of the section.

title

## Beautiful Vue UI components

    
    
    <template>
      <UPageSection title="Beautiful Vue UI components" />
    </template>
    

### Description

Use the `description` prop to set the description of the section.

description

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

    
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
      />
    </template>
    

### Headline

Use the `headline` prop to set the headline of the section.

headline

Features

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

    
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
        headline="Features"
      />
    </template>
    

### Icon

Use the `icon` prop to set the icon of the section.

icon

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

    
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
        icon="i-lucide-rocket"
      />
    </template>
    

### Features

Use the `features` prop to display a list of [PageFeature](/components/page-
feature) under the description as an array of objects with the following
properties:

  * `title?: string`
  * `description?: string`
  * `icon?: string`
  * `orientation?: 'horizontal' | 'vertical'`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

  * [](/getting-started/icons)

Icons

Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.

  * [](/getting-started/fonts)

Fonts

Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.

  * [](/getting-started/color-mode)

Color Mode

Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.

    
    
    <script setup lang="ts">
    const features = ref([
      {
        title: 'Icons',
        description: 'Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.',
        icon: 'i-lucide-smile',
        to: '/getting-started/icons'
      },
      {
        title: 'Fonts',
        description: 'Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.',
        icon: 'i-lucide-a-large-small',
        to: '/getting-started/fonts'
      },
      {
        title: 'Color Mode',
        description: 'Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.',
        icon: 'i-lucide-sun-moon',
        to: '/getting-started/color-mode'
      }
    ])
    </script>
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
        :features="features"
      />
    </template>
    

### Links

Use the `links` prop to display a list of [Button](/components/button) under
the description.

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

[Get started](/getting-started)[Explore components](/components/app)

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        to: '/getting-started',
        icon: 'i-lucide-square-play',
        color: 'neutral'
      },
      {
        label: 'Explore components',
        to: '/components/app',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
        :links="links"
      />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation with the default slot.
Defaults to `vertical`.

orientation

horizontal

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

  * [](/getting-started/icons)

Icons

Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.

  * [](/getting-started/fonts)

Fonts

Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.

  * [](/getting-started/color-mode)

Color Mode

Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.

[Explore components](/components/app)

![Illustration](https://picsum.photos/704/1294)

    
    
    <script setup lang="ts">
    const features = ref([
      {
        title: 'Icons',
        description: 'Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.',
        icon: 'i-lucide-smile',
        to: '/getting-started/icons'
      },
      {
        title: 'Fonts',
        description: 'Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.',
        icon: 'i-lucide-a-large-small',
        to: '/getting-started/fonts'
      },
      {
        title: 'Color Mode',
        description: 'Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.',
        icon: 'i-lucide-sun-moon',
        to: '/getting-started/color-mode'
      }
    ])
    const links = ref([
      {
        label: 'Explore components',
        to: '/components/app',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
        icon="i-lucide-rocket"
        orientation="horizontal"
        :features="features"
        :links="links"
      >
        <img
          src="https://picsum.photos/704/1294"
          width="352"
          height="647"
          alt="Illustration"
          class="w-full rounded-lg"
        />
      </UPageSection>
    </template>
    

### Reverse

Use the `reverse` prop to reverse the orientation of the default slot.

orientation

horizontal

reverse

true

## Beautiful Vue UI components

Nuxt UI provides a comprehensive suite of components and utilities to help you
build beautiful and accessible web applications with Vue and Nuxt.

  * [](/getting-started/icons)

Icons

Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.

  * [](/getting-started/fonts)

Fonts

Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.

  * [](/getting-started/color-mode)

Color Mode

Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.

[Explore components](/components/app)

![Illustration](https://picsum.photos/704/1294)

    
    
    <script setup lang="ts">
    const features = ref([
      {
        title: 'Icons',
        description: 'Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.',
        icon: 'i-lucide-smile',
        to: '/getting-started/icons'
      },
      {
        title: 'Fonts',
        description: 'Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.',
        icon: 'i-lucide-a-large-small',
        to: '/getting-started/fonts'
      },
      {
        title: 'Color Mode',
        description: 'Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.',
        icon: 'i-lucide-sun-moon',
        to: '/getting-started/color-mode'
      }
    ])
    const links = ref([
      {
        label: 'Explore components',
        to: '/components/app',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageSection
        title="Beautiful Vue UI components"
        description="Nuxt UI provides a comprehensive suite of components and utilities to help you build beautiful and accessible web applications with Vue and Nuxt."
        icon="i-lucide-rocket"
        orientation="horizontal"
        reverse
        :features="features"
        :links="links"
      >
        <img
          src="https://picsum.photos/704/1294"
          width="352"
          height="647"
          alt="Illustration"
          class="w-full rounded-lg"
        />
      </UPageSection>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'section'`| `any`  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`  
`icon`| | ` string`The icon displayed above the title.  
`reverse`| `false`| `boolean`Reverse the order of the default slot.  
`title`| | ` string`  
`description`| | ` string`  
`links`| | ` ButtonProps[]`Display a list of Button under the description. `{ size: 'lg' }`Show properties

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

  
`headline`| | ` string`The headline displayed above the title.  
`features`| | ` PageFeatureProps[]`Display a list of PageFeature under the description.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `icon?: string`The icon displayed next to the title when `orientation` is `horizontal` and above the title when `orientation` is `vertical`.
  * `title?: string`
  * `description?: string`
  * `orientation?: "horizontal" | "vertical"`The orientation of the page feature. Defaults to `'horizontal'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`
  * `class?: any`
  * `ui?: { root?: ClassNameValue; wrapper?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; }`

  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; wrapper?: ClassNameValue; headline?: ClassNameValue; leading?: ClassNameValue; ... 4 more ...; features?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`top`| `{}`  
`bottom`| `{}`  
`headline`| `{}`  
`leading`| `{}`  
`title`| `{}`  
`description`| `{}`  
`links`| `{}`  
`features`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageSection: {
          slots: {
            root: 'relative isolate',
            container: 'flex flex-col lg:grid py-16 sm:py-24 lg:py-32 gap-8 sm:gap-16',
            wrapper: '',
            headline: 'mb-3',
            leading: 'flex items-center mb-6',
            leadingIcon: 'size-10 shrink-0 text-primary',
            title: 'text-3xl sm:text-4xl lg:text-5xl text-pretty tracking-tight font-bold text-highlighted',
            description: 'text-base sm:text-lg text-muted',
            links: 'mt-8 flex flex-wrap gap-x-6 gap-y-3',
            features: 'mt-8 grid'
          },
          variants: {
            orientation: {
              horizontal: {
                container: 'lg:grid-cols-2 lg:items-center',
                description: 'text-pretty',
                features: 'gap-4'
              },
              vertical: {
                container: '',
                headline: 'justify-center',
                leading: 'justify-center',
                title: 'text-center',
                description: 'text-center text-balance',
                links: 'justify-center',
                features: 'sm:grid-cols-2 lg:grid-cols-3 gap-8'
              }
            },
            reverse: {
              true: {
                wrapper: 'lg:order-last'
              }
            },
            headline: {
              true: {
                headline: 'font-semibold text-primary flex items-center gap-1.5'
              }
            },
            title: {
              true: {
                description: 'mt-6'
              }
            },
            description: {
              true: ''
            },
            features: {
              true: ''
            }
          },
          compoundVariants: [
            {
              orientation: 'vertical',
              title: true,
              class: {
                features: 'mt-16'
              }
            },
            {
              orientation: 'vertical',
              description: true,
              class: {
                features: 'mt-16'
              }
            },
            {
              orientation: 'vertical',
              features: true,
              class: {
                links: 'mt-16'
              }
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
            pageSection: {
              slots: {
                root: 'relative isolate',
                container: 'flex flex-col lg:grid py-16 sm:py-24 lg:py-32 gap-8 sm:gap-16',
                wrapper: '',
                headline: 'mb-3',
                leading: 'flex items-center mb-6',
                leadingIcon: 'size-10 shrink-0 text-primary',
                title: 'text-3xl sm:text-4xl lg:text-5xl text-pretty tracking-tight font-bold text-highlighted',
                description: 'text-base sm:text-lg text-muted',
                links: 'mt-8 flex flex-wrap gap-x-6 gap-y-3',
                features: 'mt-8 grid'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center',
                    description: 'text-pretty',
                    features: 'gap-4'
                  },
                  vertical: {
                    container: '',
                    headline: 'justify-center',
                    leading: 'justify-center',
                    title: 'text-center',
                    description: 'text-center text-balance',
                    links: 'justify-center',
                    features: 'sm:grid-cols-2 lg:grid-cols-3 gap-8'
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'lg:order-last'
                  }
                },
                headline: {
                  true: {
                    headline: 'font-semibold text-primary flex items-center gap-1.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-6'
                  }
                },
                description: {
                  true: ''
                },
                features: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  orientation: 'vertical',
                  title: true,
                  class: {
                    features: 'mt-16'
                  }
                },
                {
                  orientation: 'vertical',
                  description: true,
                  class: {
                    features: 'mt-16'
                  }
                },
                {
                  orientation: 'vertical',
                  features: true,
                  class: {
                    links: 'mt-16'
                  }
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
            pageSection: {
              slots: {
                root: 'relative isolate',
                container: 'flex flex-col lg:grid py-16 sm:py-24 lg:py-32 gap-8 sm:gap-16',
                wrapper: '',
                headline: 'mb-3',
                leading: 'flex items-center mb-6',
                leadingIcon: 'size-10 shrink-0 text-primary',
                title: 'text-3xl sm:text-4xl lg:text-5xl text-pretty tracking-tight font-bold text-highlighted',
                description: 'text-base sm:text-lg text-muted',
                links: 'mt-8 flex flex-wrap gap-x-6 gap-y-3',
                features: 'mt-8 grid'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center',
                    description: 'text-pretty',
                    features: 'gap-4'
                  },
                  vertical: {
                    container: '',
                    headline: 'justify-center',
                    leading: 'justify-center',
                    title: 'text-center',
                    description: 'text-center text-balance',
                    links: 'justify-center',
                    features: 'sm:grid-cols-2 lg:grid-cols-3 gap-8'
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'lg:order-last'
                  }
                },
                headline: {
                  true: {
                    headline: 'font-semibold text-primary flex items-center gap-1.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-6'
                  }
                },
                description: {
                  true: ''
                },
                features: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  orientation: 'vertical',
                  title: true,
                  class: {
                    features: 'mt-16'
                  }
                },
                {
                  orientation: 'vertical',
                  description: true,
                  class: {
                    features: 'mt-16'
                  }
                },
                {
                  orientation: 'vertical',
                  features: true,
                  class: {
                    links: 'mt-16'
                  }
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

[PageMarqueeA component to create infinite scrolling
content.](/components/page-marquee)[PaginationA list of buttons or links to
navigate through pages.](/components/pagination)

